import { ethers } from "hardhat";

// Minimal configuration placeholder to wire defaults on localhost
// Assumes deploy.ts printed addresses or saved a JSON under deployments/

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Configurator deployer:", await deployer.getAddress());

  // In a fuller setup we'd load addresses from a file. For now, just log and exit.
  console.log("No-op configure script placeholder (add wiring here as needed).");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
