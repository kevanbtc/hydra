// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {HydraVault} from "./HydraVault.sol";

contract HydraVaultFactory {
    event VaultCreated(address indexed vault, bytes32 indexed vaultId);

    address public policyStore;
    address public riskGuardian;

    constructor(address _policyStore, address _riskGuardian) {
        policyStore = _policyStore;
        riskGuardian = _riskGuardian;
    }

    function createVault(bytes32 vaultId) external returns (address vault) {
        vault = address(new HydraVault(address(this), vaultId, policyStore, riskGuardian));
        emit VaultCreated(vault, vaultId);
    }
}
