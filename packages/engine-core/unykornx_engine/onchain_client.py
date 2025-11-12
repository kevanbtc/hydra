"""
Lightweight on-chain client stubs for interacting with HydraGrid contracts from Python.

Usage (devnet):
- Start local chain: from onchain/ run `npm run node` (or `npx hardhat node`).
- Deploy: `npm run deploy:local` to deploy core contracts and one sample vault.
- Provide RPC URL and contract addresses to PolicyClient.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

try:
    from web3 import Web3
except Exception:  # pragma: no cover - optional extra
    Web3 = None  # type: ignore


@dataclass
class OnchainConfig:
    rpc_url: str = "http://127.0.0.1:8545"
    policy_store_address: Optional[str] = None


class PolicyClient:
    """Read-only helper for MCPPolicyStore.

    Contract ABI note: this client expects the compiled ABI JSON path to be provided
    by the caller if using outside the onchain package (e.g., artifacts from Hardhat).
    """

    def __init__(self, cfg: OnchainConfig, abi: Optional[list[dict[str, Any]]] = None):
        if Web3 is None:
            raise RuntimeError("web3 is not installed. Install with `pip install unykornx-hydragrid[onchain]`.")
        self.w3 = Web3(Web3.HTTPProvider(cfg.rpc_url))
        if not self.w3.is_connected():
            raise RuntimeError(f"Cannot connect to RPC at {cfg.rpc_url}")
        if not cfg.policy_store_address:
            raise ValueError("policy_store_address must be provided")
        if abi is None:
            raise ValueError("ABI for MCPPolicyStore must be provided")
        self.contract = self.w3.eth.contract(address=cfg.policy_store_address, abi=abi)

    def get_policy(self, vault_address: str) -> dict[str, Any]:
        """Return the policy struct for a given vault address.

        Returns a dict shaped like Solidity MCPPolicy:
        { policyId: bytes32, weights: [{strategyId, bps}], timestamp: int, validUntil: int }
        """
        policy_tuple = self.contract.functions.policy(vault_address).call()
        # Web3 decodes structs to tuples; map to dict lazily.
        policy_id, weights_raw, timestamp, valid_until = policy_tuple
        weights = [
            {"strategyId": w[0], "bps": int(w[1])}  # type: ignore[index]
            for w in weights_raw
        ]
        return {
            "policyId": policy_id,
            "weights": weights,
            "timestamp": int(timestamp),
            "validUntil": int(valid_until),
        }
