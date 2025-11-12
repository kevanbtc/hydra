import { ethers } from "hardhat";

async function main() {
  const [deployer, gov, riskOracle, mcpSigner, reporter] = await ethers.getSigners();

  console.log("Deployer:", await deployer.getAddress());

  // Governance placeholder
  const Governance = await ethers.getContractFactory("Governance");
  const governance = await Governance.deploy(await gov.getAddress());
  await governance.waitForDeployment();
  console.log("Governance:", await governance.getAddress());

  // MCP Policy Store + Oracle
  const MCPPolicyStore = await ethers.getContractFactory("MCPPolicyStore");
  const policyStore = await MCPPolicyStore.deploy(ethers.ZeroAddress);
  await policyStore.waitForDeployment();
  console.log("MCPPolicyStore:", await policyStore.getAddress());

  const MCPOracle = await ethers.getContractFactory("MCPOracle");
  const oracle = await MCPOracle.deploy(await policyStore.getAddress(), await gov.getAddress());
  await oracle.waitForDeployment();
  console.log("MCPOracle:", await oracle.getAddress());

  // Wire oracle into policy store (constructor-only in stub; left as-is)
  // RiskGuardian
  const RiskGuardian = await ethers.getContractFactory("RiskGuardian");
  const riskGuardian = await RiskGuardian.deploy(await gov.getAddress(), await riskOracle.getAddress());
  await riskGuardian.waitForDeployment();
  console.log("RiskGuardian:", await riskGuardian.getAddress());

  // Strategy Registry
  const StrategyRegistry = await ethers.getContractFactory("StrategyRegistry");
  const registry = await StrategyRegistry.deploy(await gov.getAddress());
  await registry.waitForDeployment();
  console.log("StrategyRegistry:", await registry.getAddress());

  // Factory
  const HydraVaultFactory = await ethers.getContractFactory("HydraVaultFactory");
  const factory = await HydraVaultFactory.deploy(await policyStore.getAddress(), await riskGuardian.getAddress());
  await factory.waitForDeployment();
  console.log("HydraVaultFactory:", await factory.getAddress());

  // Create a sample vault
  const vaultId = ethers.id("HV-ALPHA-001");
  const tx = await factory.createVault(vaultId);
  const rc = await tx.wait();
  const ev = rc!.logs.map(l => {
    try { return (l as any).args; } catch { return undefined; }
  }).find(Boolean) as any;
  const vaultAddr = ev?.vault ?? (rc!.logs[0] as any)?.args?.vault;
  console.log("Sample HydraVault:", vaultAddr);

  console.log("Done.");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
