import json

from evmosproto.cosmos.staking.v1beta1.tx_pb2 import MsgDelegate
from evmosproto.cosmos.staking.v1beta1.tx_pb2 import MsgUndelegate
from google.protobuf.json_format import Parse

from evmosgrpc.constants import DENOM


def create_msg_delegate(delegator, validator, amount, denom=DENOM):
    raw_msg = {
        'delegatorAddress': delegator,
        'validatorAddress': validator,
        'amount': {
            'denom': denom,
            'amount': str(amount),
        },
    }
    return Parse(json.dumps(raw_msg), MsgDelegate())


def create_msg_undelegate(delegator, validator, amount, denom=DENOM):
    raw_msg = {
        'delegatorAddress': delegator,
        'validatorAddress': validator,
        'amount': {
            'denom': denom,
            'amount': str(amount),
        },
    }
    return Parse(json.dumps(raw_msg), MsgUndelegate())
