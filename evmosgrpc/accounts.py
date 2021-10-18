from google.protobuf.json_format import MessageToDict

from evmosproto.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from evmosproto.cosmos.auth.v1beta1.query_pb2_grpc import QueryStub
from evmosproto.ethermint.types.v1.account_pb2 import EthAccount
from typing import Union
from evmosgrpc.utils import create_grpc_channel


# Get account, returns pub_key, account_number, sequence
def get_account_grpc(account: str) -> Union[tuple[str, str], tuple[None, None]]:
    # Create channel
    stub = QueryStub(create_grpc_channel())
    params = QueryAccountRequest()
    params.address = account
    # Send the request
    resp = stub.Account(params)
    # Parse the Any message
    account = EthAccount()
    account.ParseFromString(resp.account.value)
    account = MessageToDict(account, including_default_value_fields=True)['baseAccount']
    return account['accountNumber'], account['sequence']
