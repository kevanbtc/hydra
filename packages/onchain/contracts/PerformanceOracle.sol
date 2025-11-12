// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

struct PerformanceSnapshot {
    bytes32 vaultId;
    uint64 timestamp;
    int256 dailyReturnBps;
    uint256 nav;
}

contract PerformanceOracle {
    mapping(bytes32 => PerformanceSnapshot) public lastSnapshot;
    mapping(address => bool) public reporters;
    address public gov;

    modifier onlyGov() { require(msg.sender == gov, "NOT_GOV"); _; }

    constructor(address _gov) { gov = _gov; }

    function setReporter(address reporter, bool allowed) external onlyGov {
        reporters[reporter] = allowed;
    }

    function submitSnapshot(PerformanceSnapshot calldata snap, bytes calldata /*signature*/) external {
        // signature verification omitted in stub
        require(reporters[msg.sender], "NOT_REPORTER");
        lastSnapshot[snap.vaultId] = snap;
    }
}
