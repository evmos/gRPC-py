from evmosgrpc.messages.msgsend import create_msg_send


def test_create_msg_send():
    a = create_msg_send('evmos1h8057cmr2znknsaqu6vqazfughcfq93k24dmw4', 'evmos1dlt6lgs6sslurfl3zyl7tgmnvzhq5us2uquxv7',
                        100, 'evmos')
    assert a.SerializeToString(
    ) == b'\n,evmos1h8057cmr2znknsaqu6vqazfughcfq93k24dmw4\x12,evmos1dlt6lgs6sslurfl3zyl7tgmnvzhq5us2uquxv7\x1a\x0c\n\x05evmos\x12\x03100'  # NOQA E501
