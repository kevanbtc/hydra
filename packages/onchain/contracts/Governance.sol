// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @notice Minimal governance placeholder; replace with OZ Governor + Timelock in production.
contract Governance {
    address public chair;

    modifier onlyChair() { require(msg.sender == chair, "NOT_CHAIR"); _; }

    constructor(address _chair) { chair = _chair; }

    function transferChair(address newChair) external onlyChair { chair = newChair; }
}
