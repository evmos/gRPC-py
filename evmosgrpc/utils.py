import grpc

from evmosgrpc.constants import GRPC_ENDPOINT


def create_grpc_channel(endpoint=GRPC_ENDPOINT):
    return grpc.insecure_channel(endpoint)
