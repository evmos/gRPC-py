import json

from evmosproto.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from google.protobuf.json_format import Parse

from evmosgrpc.constants import DENOM


def create_msg_send(origin, dest, amount, denom=DENOM):
    raw_msg = {
        'fromAddress': origin,
        'toAddress': dest,
        'amount': [{
            'denom': denom,
            'amount': str(amount),
        }],
    }
    return Parse(json.dumps(raw_msg), MsgSend())
