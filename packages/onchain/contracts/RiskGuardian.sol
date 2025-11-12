// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

struct RiskLimits {
    uint256 maxLeverageBps;
    int256 maxDrawdownBps;
    uint256 maxSingleAssetExposureBps;
}

contract RiskGuardian {
    address public gov;
    mapping(address => RiskLimits) public vaultLimits;
    mapping(address => bool) public isVaultPaused;
    address public riskOracle;

    modifier onlyGov() { require(msg.sender == gov, "NOT_GOV"); _; }
    modifier onlyRiskOracle() { require(msg.sender == riskOracle, "NOT_RISK_ORACLE"); _; }

    constructor(address _gov, address _riskOracle) {
        gov = _gov;
        riskOracle = _riskOracle;
    }

    function setVaultLimits(address vault, RiskLimits calldata limits) external onlyGov {
        vaultLimits[vault] = limits;
    }

    function reportRisk(address vault, int256 realizedDrawdownBps, uint256 leverageBps) external onlyRiskOracle {
        RiskLimits memory lim = vaultLimits[vault];
        if (realizedDrawdownBps <= -lim.maxDrawdownBps) {
            isVaultPaused[vault] = true;
        }
        if (leverageBps > lim.maxLeverageBps) {
            isVaultPaused[vault] = true;
        }
    }

    function isTradingAllowed(address vault) external view returns (bool) {
        return !isVaultPaused[vault];
    }
}
