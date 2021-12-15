import json

from evmosproto.cosmos.base.v1beta1.coin_pb2 import Coin
from evmosproto.cosmos.gov.v1beta1.query_pb2 import QueryProposalsRequest
from evmosproto.cosmos.gov.v1beta1.query_pb2_grpc import QueryStub
from evmosproto.cosmos.gov.v1beta1.tx_pb2 import MsgSubmitProposal
from evmosproto.cosmos.gov.v1beta1.tx_pb2 import MsgVote
from evmosproto.google.protobuf.any_pb2 import Any
from google.protobuf.json_format import MessageToDict
from google.protobuf.json_format import Parse

from evmosgrpc.constants import DENOM
from evmosgrpc.constants import PROPOSAL_MIN_AMOUNT
from evmosgrpc.messages.irm import create_register_coin_proposal
from evmosgrpc.messages.irm import create_register_erc20_proposal
from evmosgrpc.utils import create_grpc_channel


def create_submit_proposal(content, initial_deposit, proposer):
    raw_msg = {
        'content': MessageToDict(content),
        'initial_deposit': [MessageToDict(initial_deposit)],
        'proposer': proposer
    }
    return Parse(json.dumps(raw_msg), MsgSubmitProposal())


def register_erc20_proposal_message(wallet, contract, title, description):
    proposal = create_register_erc20_proposal(title, description, contract)
    any = Any()
    any.Pack(proposal, type_url_prefix='/')
    coin = Coin()
    coin.denom = DENOM
    coin.amount = PROPOSAL_MIN_AMOUNT
    p = create_submit_proposal(any, coin, wallet)
    return p


def register_coin_proposal_message(wallet, metadata, title, description):
    proposal = create_register_coin_proposal(title, description, metadata)

    any = Any()
    any.Pack(proposal, type_url_prefix='/')
    coin = Coin()
    coin.denom = DENOM
    coin.amount = PROPOSAL_MIN_AMOUNT
    p = create_submit_proposal(any, coin, wallet)
    return p


def toggle_token_proposal_message(wallet, toggle_token):
    any = Any()
    any.Pack(toggle_token, type_url_prefix='/')
    coin = Coin()
    coin.denom = DENOM
    coin.amount = PROPOSAL_MIN_AMOUNT
    p = create_submit_proposal(any, coin, wallet)
    return p


def update_token_pair_erc20_proposal_message(wallet, update_token):
    any = Any()
    any.Pack(update_token, type_url_prefix='/')
    coin = Coin()
    coin.denom = DENOM
    coin.amount = PROPOSAL_MIN_AMOUNT
    p = create_submit_proposal(any, coin, wallet)
    return p


def get_proposals():
    stub = QueryStub(create_grpc_channel())
    params = QueryProposalsRequest()
    resp = stub.Proposals(params)
    return resp


def create_vote_message(proposal_id: int, voter: str, option: int):
    message = {
        'proposal_id': proposal_id,
        'voter': voter,
        'option': option,
    }
    return Parse(json.dumps(message), MsgVote())
