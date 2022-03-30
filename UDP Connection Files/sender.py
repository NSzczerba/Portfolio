import socket

SERVER_NAME_STR = '10.128.0.3'
SERVER_PORT_INT = 12000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(("10.128.0.2", 12001))
        tx_message_str = "PURPLE PEOPLE"

        print("TX: ", tx_message_str)
        print("TO: ", (SERVER_NAME_STR, SERVER_PORT_INT))
        client_socket.sendto(tx_message_str.encode(), (SERVER_NAME_STR, SERVER_PORT_INT))
        print("...sent...")
        print("...waiting...")
        rx_message_bytes, server_address = client_socket.recvfrom(2048)
        print("RX: ", rx_message_bytes.decode())
        print("FROM: ", server_address)
