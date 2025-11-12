import { expect } from "chai";
import { ethers } from "hardhat";

describe("HydraVault end-to-end stub", () => {
  it("deploys factory and creates a vault", async () => {
    const [deployer, gov, riskOracle] = await ethers.getSigners();

    const MCPPolicyStore = await ethers.getContractFactory("MCPPolicyStore");
    const policyStore = await MCPPolicyStore.deploy(ethers.ZeroAddress);
    await policyStore.waitForDeployment();

    const RiskGuardian = await ethers.getContractFactory("RiskGuardian");
    const riskGuardian = await RiskGuardian.deploy(await gov.getAddress(), await riskOracle.getAddress());
    await riskGuardian.waitForDeployment();

    const HydraVaultFactory = await ethers.getContractFactory("HydraVaultFactory");
    const factory = await HydraVaultFactory.deploy(await policyStore.getAddress(), await riskGuardian.getAddress());
    await factory.waitForDeployment();

    const vaultId = ethers.id("HV-ALPHA-TEST");
    const tx = await factory.createVault(vaultId);
    const rc = await tx.wait();
    expect(rc?.status).to.eq(1);
  });
});
