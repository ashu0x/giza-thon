from giza.agents import GizaAgent
import numpy as np
from addresses import ADDRESSES
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from ape import Contract, accounts, networks

load_dotenv(find_dotenv())

def predict(agent: GizaAgent, X: np.ndarray):
    prediction = agent.predict(input_feed={"val": X}, verifiable=True,dry_run=True)
    print("Prediction: ", prediction)
    return prediction

def create_agent(agent_id: int, chain: str, contracts: dict, account_alias: str):
    """
    Create a Giza agent for the Pendle protocol
    """
    agent = GizaAgent.from_id(
        id=agent_id,
        contracts=contracts,
        chain=chain,
        account=account_alias,
    )
    return agent

def get_data():
    df = pd.read_csv("x_test.csv")
    return df

def main():
    contracts = {
        "eigen_delegation_manager": ADDRESSES['eigen_delegation_manager'],
        "eigen_strategy_manager": ADDRESSES['eigen_strategy_manager'],
        "stETH": ADDRESSES['stETH'],
        
    }
    
    agent = create_agent(agent_id=100, chain="ethereum:mainnet-fork:foundry", contracts=contracts, account_alias="ash")
    
    df = get_data()
    features = ['lag_1', 'lag_2', 'lag_3', 'lag_4', 'lag_5', 'lag_6', 'lag_7', 'quorum_id', 'total_batches', 'total_unsigned_batches', 'frequency', 'total_percentage']
    X = df[features].values.astype(np.float32)
    
    result = predict(agent, X)
    
    with agent.execute() as contracts:
        operator = df.iloc[np.argmin(result.value.flatten())]
        print(f"Operator with the min predicted percentage: {operator['operator_address']} with a predicted percentage of {result.value.flatten().min()}")
        stETH = contracts.stETH
        stETH_decimals = stETH.decimals()
        stake_stETH_amount = 1 * (10**stETH_decimals)  ## Mint 10 stETH
        
        dev = accounts.load("ash")
        stETH_balance = stETH.balanceOf(dev)
        
        print(f"Dev Wallet has a balance of {stETH_balance/10**stETH_decimals} stETH")
        
        # Approve the stETH contract to spend the stETH
        tx1 = stETH.approve(ADDRESSES['eigen_strategy_manager'], stake_stETH_amount)

        # Deposit the stETH into the strategy
    
        tx2 = contracts.eigen_strategy_manager.depositIntoStrategy(ADDRESSES['eigen_stETH_strategy'], ADDRESSES['stETH'], stake_stETH_amount)
        
        # Stake the stETH to operator
        tx3 = contracts.eigen_delegation_manager.delegateTo(operator['operator_address'], ('0x', 0), '0x0000000000000000000000000000000000000000000000000000000000000000')
        stETH_balance = stETH.balanceOf(dev)
        
        print(f"Dev Wallet has a balance of {stETH_balance/10**stETH_decimals} stETH after staking")
    
main()

#Logs

# INFO: Connecting to existing Geth node at https://ethereum-rpc.publicnode.com/[hidden].
# WARNING: Danger! This account will now sign any transaction it's given.
# Dry run enabled. Skipping verification.
# Operator with the min predicted percentage: 0x5d4b5ef127c545e5bf8e247f9fcd4e75a0a366b4 with a predicted percentage of -0.0072174072265625
# Dev Wallet has a balance of 10.0 stETH
# WARNING: Using cached key for ash
# INFO: Confirmed 0x45124e9c3c41623a4da54b6e9912bfb4eefb1a634498933043008236c1e5b4e3 (total fees paid = 584219287819596)
# WARNING: Using cached key for ash
# INFO: Confirmed 0x101da8877dfa73bb912f9a7a3f4a3b1bd0c701c06ea5feb30a04d0dd50cbeb25 (total fees paid = 1699233243891150)
# WARNING: Using cached key for ash
# INFO: Confirmed 0x2c234d2c96c830b0c09513586e1c49552add33fae45c4f342809c1894699a1ef (total fees paid = 845323762477088)
# Dev Wallet has a balance of 9.0 stETH after staking