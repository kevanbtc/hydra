// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {MCPPolicy, MCPPolicyStore} from "./MCPPolicyStore.sol";

contract MCPOracle {
    mapping(address => bool) public signers; // whitelisted MCP off-chain signers
    MCPPolicyStore public policyStore;
    address public gov;

    modifier onlyGov() { require(msg.sender == gov, "NOT_GOV"); _; }

    constructor(address _policyStore, address _gov) {
        policyStore = MCPPolicyStore(_policyStore);
        gov = _gov;
    }

    function setSigner(address signer, bool allowed) external onlyGov {
        signers[signer] = allowed;
    }

    function submitPolicy(
        address vault,
        MCPPolicy calldata policy_,
        bytes calldata /*signature*/
    ) external {
        // NOTE: signature verification omitted in stub
        // require(signers[recoveredSigner], "UNAUTHORIZED_SIGNER");
        policyStore.setPolicy(vault, policy_);
    }
}
