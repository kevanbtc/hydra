// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

struct StrategyMeta {
    bytes32 id;
    uint8 classId;
    bool enabled;
}

contract StrategyRegistry {
    mapping(bytes32 => StrategyMeta) public strategies;
    address public gov;

    modifier onlyGov() { require(msg.sender == gov, "NOT_GOV"); _; }

    constructor(address _gov) { gov = _gov; }

    function registerStrategy(StrategyMeta calldata meta) external onlyGov {
        strategies[meta.id] = meta;
    }

    function setStrategyEnabled(bytes32 id, bool enabled) external onlyGov {
        StrategyMeta storage m = strategies[id];
        m.enabled = enabled;
    }
}
