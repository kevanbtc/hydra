// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

struct StrategyWeight {
    bytes32 strategyId;
    uint16 bps; // 0-10_000
}

struct MCPPolicy {
    bytes32 policyId;
    StrategyWeight[] weights;
    uint64 timestamp;
    uint64 validUntil;
}

contract MCPPolicyStore {
    mapping(address => MCPPolicy) internal _policies; // vault => policy
    address public oracle;

    modifier onlyOracle() { require(msg.sender == oracle, "NOT_ORACLE"); _; }

    constructor(address _oracle) {
        oracle = _oracle;
    }

    function policy(address vault) external view returns (MCPPolicy memory) {
        return _policies[vault];
    }

    function setPolicy(address vault, MCPPolicy calldata policy_) external onlyOracle {
        _policies[vault] = policy_;
    }
}
