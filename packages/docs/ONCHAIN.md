# On-Chain Contracts and Dev Workflow

This document describes the HydraGrid on-chain components, how they connect to off-chain systems, and the local dev workflow.

## Contracts

- HydraVault: ERC20 share token representing a managed portfolio; holds off-chain custody in v1.
- HydraVaultFactory: Creates new HydraVaults, wiring risk and policy stores.
- StrategyRegistry: Registry of strategy IDs, classes, and enabled flags.
- MCPPolicyStore: Stores per-vault policy payloads signed by off-chain MCP.
- MCPOracle: Accepts MCP policies from whitelisted signers and writes to MCPPolicyStore.
- RiskGuardian: Stores risk limits and can pause vaults when limits are breached.
- PerformanceOracle: Records performance snapshots per vaultId.
- Governance: Minimal placeholder for role control; replace with OZ Governor in production.
- TokenHYDRA: Placeholder governance/staking token (optional for v1).

## Off-chain ↔ On-chain Flow (v1)

- MCP agents sign policy updates off-chain; a whitelisted MCP signer submits to MCPOracle.
- MCPOracle validates (signature verification TBD) and writes to MCPPolicyStore.
- Engine checks RiskGuardian.isTradingAllowed(vault) before placing trades.
- Analytics reads PerformanceOracle and MCPPolicyStore for UI and reports.

## Local Dev

1. From `packages/onchain/`:
   - Install deps: `npm install`
   - Compile: `npx hardhat compile`
   - Test: `npx hardhat test`
2. Run a local chain: `npx hardhat node`
3. Deploy to local: `npm run deploy:local`

## Python Integration

- Optional extras: install `pip install -e .[onchain]`
- Use `unykornx_engine.onchain_client.PolicyClient` with a local RPC URL and the MCPPolicyStore ABI.

## Notes

- OpenZeppelin Contracts v5 used for ERC20.
- Solidity 0.8.20, optimizer enabled.
- Replace Governance with OZ Governor + Timelock for production.
