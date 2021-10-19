from evmoswallet import Wallet
from google.protobuf.message import Message

from evmosgrpc.accounts import get_account_grpc
from evmosgrpc.broadcaster import broadcast


class TransactionBuilder():
    def __init__(self, seed: str) -> None:
        self.wallet = Wallet(seed)
        self.address = self.wallet.evmos_address
        self.account_number, self.sequence = get_account_grpc(self.address)

    def send_tx(self, msg: Message):
        self.update_sequence()
        return broadcast(msg)

    def update_sequence(self):
        _, self.sequence = get_account_grpc(self.address)
