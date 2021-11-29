import os

GRPC_ENDPOINT = os.getenv('GRPC_ENDPOINT', '127.0.0.1:9090')
MEMO = os.getenv('MEMO', '')
FEE = os.getenv('FEE', '1000')
GAS_LIMIT = os.getenv('GAS_LIMIT', '100000')
CHAIN_ID = os.getenv('CHAIN_ID', 'evmos_9000-2')
DENOM = os.getenv('DENOM', 'aphoton')

# Types
ETHSECP256K1 = 'ethsecp256k1'
SECP256K1 = 'secp256k1'
