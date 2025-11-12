// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @title HYDRA Token (placeholder)
/// @notice v1 stub for governance + staking future extension.
contract TokenHYDRA is ERC20 {
    address public minter;

    modifier onlyMinter() { require(msg.sender == minter, "NOT_MINTER"); _; }

    constructor(address _minter) ERC20("HYDRA", "HYDRA") {
        minter = _minter;
        _mint(_minter, 1_000_000 ether); // initial supply stub
    }

    function mint(address to, uint256 amount) external onlyMinter {
        _mint(to, amount);
    }
}
