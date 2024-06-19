import os
from logging import getLogger

from addresses import ADDRESSES
from ape import Contract, accounts, networks
from dotenv import find_dotenv, load_dotenv

# logging.basicConfig(level=logging.INFO)

load_dotenv(find_dotenv())

dev_passphrase = os.environ.get(
    "DEV_PASSPHRASE"
)  ## Make sure to edit your .env file with your passphrase
network = "ethereum:mainnet-fork:foundry"  ## We ask the Ape Framework to locate our forked mainnet

if __name__ == "__main__":

    logger = getLogger("setup_logger")
    logger.propagate = False

    logger.warning("Initiationg setup process")

    networks.parse_network_choice(network).__enter__()

    stETH = Contract(ADDRESSES["stETH"])
    stETH_decimals = stETH.decimals()

    dev = accounts.load("ash")  ## Change this to your account name
    dev.set_autosign(True, passphrase=dev_passphrase)
    dev.balance += 20 * int(1e18)  # Add 20 ETH to the account

    stETH_mint_amount = 10 * (10**stETH_decimals)  ## Mint 10 stETH

    with accounts.use_sender("ash"):
        logger.warning(
            f"Staking Ether to get  {stETH_mint_amount/10**stETH_decimals} stETH"
        )
        stETH.submit(
            "0x0000000000000000000000000000000000000000", value=stETH_mint_amount, max_fee=10**10
        )  ## Deposit 10 ETH to get stETH
        stETH_balance = stETH.balanceOf(dev)

    logger.warning(
        f"Dev Wallet has a balance of {stETH_balance/10**stETH_decimals} stETH"
    )
    logger.warning("Setup complete")
    
# Logs

# Initiationg setup process
# INFO: Connecting to existing Erigon node at https://rpc.mevblocker.io/[hidden].
# WARNING: Danger! This account will now sign any transaction it's given.
# Staking Ether to get  10.0 stETH
# WARNING: Using cached key for ash
# INFO: Confirmed 0x0b10f59e722caf23e4e909f0b3203b9d1c05616d17384df40c73a6ceeacadf9c (total fees paid = 981577518484598)
# Dev Wallet has a balance of 10.0 stETH
# Setup complete