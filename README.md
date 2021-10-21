# Evmos GRPC

[![PyPI version](https://badge.fury.io/py/evmosgrpc.svg)](https://badge.fury.io/py/evmosgrpc) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hanchon-live/evmosgrpc/master.svg)](https://results.pre-commit.ci/latest/github/hanchon-live/evmosgrpc/master)

Evmos' grpc messages.
WIP: Only the `message send` was implemented because is the one used for the faucet.

## Requirements

- Python3.9+
- Evmos grpc endpoint available
- Wallet seed (only supports the evmos default algorithm: `ethsecp256k1`)

## Installation

```sh
pip install evmosgrpc
```

## Configuration

The configuration can be set using `env vars`:

- GRPC_ENDPOINT: Default = '127.0.0.1:9090'
- MEMO: Default = 'Sent from Hanchon\'s faucet'
- FEE: Default = '20'
- GAS_LIMIT: Default = '200000'
- CHAIN_ID: Default = 'evmos_9000-1'
- DENOM: Default = 'aphoton'

## Usage

```python
from evmosgrpc.messages.msgsend import create_msg_send
from evmosgrpc.builder import TransactionBuilder
from evmosgrpc.transaction import Transaction

seed = 'garment seat help gallery ride divide truth smooth end chunk '\
       'ten cross badge want vehicle mirror dismiss remind crouch '\
       'base crouch palm leader dinner'
builder = TransactionBuilder(seed)
msg = create_msg_send(
    builder.address,
    "evmos1sgg7ny6mkk375ghdlx837hkm92dqxs450fxwwz",
    100,
)
res = builder.send_tx(Transaction().generate_tx(builder, msg))
# res =
# tx_response {
#   txhash: "F4DFCF8E0BAEBBE088DF0C8A4DA1EF70CD29983C5F7663A523A87F1CE479BFF5"
#   raw_log: "[]"
# }

# To read the response as a dict:
from google.protobuf.json_format import MessageToDict
res_obj = MessageToDict(res)
```

## TODO

- Add tests.
- Add more messages.
- Add `secp256k1` wallet support on `evmoswallet`.
