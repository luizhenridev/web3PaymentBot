import solcx 
from pathlib import Path

solcx.install_solc('0.8.26')

contract_path = Path('./contracts') / 'payment.sol'

with open(contract_path, "r") as file:
    contract_source = file.read()

compiled_sol = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {"payment.sol":{"content": contract_source}},
        "settings": {
            "outputSelection":{
                "*":{"*":["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            },
            "viaIR":True
        },
    },
    solc_version = "0.8.26"
)

print(compiled_sol)