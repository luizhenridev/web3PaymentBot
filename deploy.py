from web3 import Web3
import os
from pathlib import Path
from dotenv import load_dotenv
from compile import compiled_sol
from mnemonic import Mnemonic


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_URL = os.environ.get('URL_SEPOLIA') 
private_key = os.getenv("MNEMONIC_ACCOUNT")

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

mnemo = Mnemonic("english")
seed = mnemo.to_seed(private_key)
short_seed = seed[:32]
hexSeed = short_seed.hex()

account = web3.eth.account.from_key(hexSeed)


contract = web3.eth.contract(abi=compiled_sol['contracts']['payment.sol']['Coin']['abi'], bytecode=compiled_sol['contracts']['payment.sol']['Coin']['evm']['bytecode']['object'])
tx_data = contract.constructor().build_transaction({
    'from': account.address,
    'nonce': web3.eth.get_transaction_count(account.address),
    'gas': 79756,
    'gasPrice': web3.to_wei(21, 'gwei')
})

signed_tx = web3.eth.account.sign_transaction(tx_data, hexSeed)
tx_hash = web3.eth._send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt['contractAddress']

print(contract_address)