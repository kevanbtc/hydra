// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @title HydraVault
/// @notice Tokenized representation of an off-chain managed strategy mix.
contract HydraVault is ERC20 {
    address public immutable factory;
    bytes32 public vaultId;
    address public policyStore;
    address public riskGuardian;

    enum Status { LIVE, PAUSED, SETTLING }
    Status public status;

    uint256 public nav; // last reported NAV (scaled, e.g., 1e18)

    modifier onlyFactory() { require(msg.sender == factory, "NOT_FACTORY"); _; }

    constructor(address _factory, bytes32 _vaultId, address _policyStore, address _riskGuardian) ERC20("Hydra Vault Share", "HVSH") {
        factory = _factory;
        vaultId = _vaultId;
        policyStore = _policyStore;
        riskGuardian = _riskGuardian;
        status = Status.LIVE;
    }

    function deposit(uint256 /*amount*/) external {
        // placeholder: off-chain custody for now
        // mint shares 1:1 amount assumption for stub
        _mint(msg.sender, 1e18); // dummy value
    }

    function withdraw(uint256 shares) external {
        _burn(msg.sender, shares);
        // off-chain settlement in v1 stub
    }

    function updateNav(uint256 newNav) external {
        // TODO: access control (MCP performance oracle / reporter)
        nav = newNav;
    }
}
