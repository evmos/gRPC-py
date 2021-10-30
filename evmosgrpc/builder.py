from evmoswallet import Wallet
from google.protobuf.message import Message

from evmosgrpc.accounts import get_account_grpc
from evmosgrpc.broadcaster import broadcast

from evmosgrpc.constants import ETHSECP256K1
from evmosgrpc.constants import SECP256K1


class TransactionBuilder():
    def __init__(self, seed: str) -> None:
        self.wallet = Wallet(seed)
        self.algo = ETHSECP256K1
        self.address = self.wallet.evmos_address
        self.account_number, self.sequence = get_account_grpc(self.address)

    def send_tx(self, msg: Message):
        self.update_sequence()
        return broadcast(msg)

    def update_sequence(self):
        _, self.sequence = get_account_grpc(self.address)


class PubkeyWallet():
    def __init__(self, pubkey) -> None:
        self.public_key = pubkey


class KeplrWallet(TransactionBuilder):
    def __init__(self, address: str, algo: str = SECP256K1, pubkey=None) -> None:
        self.wallet = PubkeyWallet(pubkey)
        self.algo = algo
        self.address = address
        self.account_number, self.sequence = get_account_grpc(self.address)
