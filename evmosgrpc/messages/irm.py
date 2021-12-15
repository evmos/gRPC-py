import json

from evmosproto.evmos.intrarelayer.v1.intrarelayer_pb2 import RegisterCoinProposal
from evmosproto.evmos.intrarelayer.v1.intrarelayer_pb2 import RegisterERC20Proposal
from evmosproto.evmos.intrarelayer.v1.intrarelayer_pb2 import ToggleTokenRelayProposal
from evmosproto.evmos.intrarelayer.v1.intrarelayer_pb2 import UpdateTokenPairERC20Proposal
from evmosproto.evmos.intrarelayer.v1.tx_pb2 import MsgConvertCoin
from evmosproto.evmos.intrarelayer.v1.tx_pb2 import MsgConvertERC20
from google.protobuf.json_format import Parse


def create_register_erc20_proposal(title, description, erc20address):
    raw_msg = {'title': title, 'description': description, 'erc20address': erc20address}
    return Parse(json.dumps(raw_msg), RegisterERC20Proposal())


def create_register_coin_proposal(title, description, metadata):
    raw_msg = {'title': title, 'description': description, 'metadata': metadata}
    return Parse(json.dumps(raw_msg), RegisterCoinProposal())


def create_convert_erc20_message(contract: str, amount: str, receiver: str, sender: str):
    raw_msg = {'contract_address': contract, 'amount': amount, 'receiver': receiver, 'sender': sender}
    return Parse(json.dumps(raw_msg), MsgConvertERC20())


def create_convert_coin_message(denom: str, amount: str, receiver: str, sender: str):
    raw_msg = {
        'coin': {
            'denom': denom,
            'amount': amount,
        },
        'receiver': receiver,
        'sender': sender
    }
    return Parse(json.dumps(raw_msg), MsgConvertCoin())


def create_toggle_token_proposal(title, description, token):
    raw_msg = {'title': title, 'description': description, 'token': token}
    return Parse(json.dumps(raw_msg), ToggleTokenRelayProposal())


def create_update_token_pair_proposal(title, description, old_address, new_address):
    raw_msg = {
        'title': title,
        'description': description,
        'erc20_address': old_address,
        'new_erc20_address': new_address
    }
    return Parse(json.dumps(raw_msg), UpdateTokenPairERC20Proposal())


def get_IRM_proposals(proposals):
    ret = []
    for p in proposals:
        if (p.content.type_url == '/evmos.intrarelayer.v1.RegisterCoinProposal'
                or p.content.type_url == '/evmos.intrarelayer.v1.RegisterERC20'):
            ret.append({
                'id': p.proposal_id,
                'type': p.content.type_url,
                'value': p.content.value,
                'status': p.status,
                'total_deposit': p.total_deposit[0].amount,
                'voting_start_time': f'{p.voting_start_time.seconds}/{p.voting_start_time.nanos}',
                'voting_end_time': f'{p.voting_end_time.seconds}/{p.voting_end_time.nanos}',
                'final_tally_result': {
                    'abstain': p.final_tally_result.abstain,
                    'no': p.final_tally_result.no,
                    'yes': p.final_tally_result.yes,
                    'no_with_veto': p.final_tally_result.no_with_veto,
                }
            })

    return ret
