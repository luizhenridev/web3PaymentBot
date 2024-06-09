from web3 import Web3
import os
from pathlib import Path
from dotenv import load_dotenv
from compile import compiled_sol
from mnemonic import Mnemonic


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_URL = os.environ.get('URL_SEPOLIA') 
private_key = os.getenv("PRIVATE_KEY")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
check = web3.is_connected()

account = web3.eth.account.from_key(private_key)

address = account.address
contract_abi = compiled_sol['contracts']['payment.sol']['Coin']['abi']
contract_bytecode = compiled_sol['contracts']['payment.sol']['Coin']['evm']['bytecode']['object']

contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)


contract_tx = contract.constructor().build_transaction({
    'from': address,
    'nonce': web3.eth.get_transaction_count(address),
    'gas':2000000,
    'gasPrice': web3.eth.gas_price,
})

signed_txn = web3.eth.account.sign_transaction(contract_tx, private_key=private_key)

txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

print(f'Contract deployed at address: {txn_receipt.contractAddress}')

