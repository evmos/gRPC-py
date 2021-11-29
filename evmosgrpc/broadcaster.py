from evmosproto.cosmos.tx.v1beta1.service_pb2 import BROADCAST_MODE_SYNC
from evmosproto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest
from evmosproto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub
from google.protobuf.message import Message

from evmosgrpc.utils import create_grpc_channel


def create_broadcast_tx(tx: Message, mode=BROADCAST_MODE_SYNC):
    broadcast_tx = BroadcastTxRequest()
    broadcast_tx.tx_bytes = tx.SerializeToString()
    broadcast_tx.mode = mode
    return broadcast_tx


def broadcast(tx: Message, mode=BROADCAST_MODE_SYNC):
    tx = create_broadcast_tx(tx, mode)
    channel = create_grpc_channel()
    stub = ServiceStub(channel)
    return stub.BroadcastTx(tx)
