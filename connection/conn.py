from web3 import Web3
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

INFURA_URL = os.environ.get('URL_SEPOLIA') 

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

print(web3.isConnected())