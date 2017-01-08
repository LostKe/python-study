# coding=utf-8

import socket, threading

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '115.159.91.135'

socket_client.connect((server_address, 9999))


# 接收消息
def recevice_msg():
    while True:
        data = socket_client.recv(1024)
        print(data.decode('utf-8'))


# 发送消息
def send_msg():
    for msg in [b'linux', b'android', b'java', b'php']:
        socket_client.send(msg)
    socket_client.send(b'exit')
    # socket_client.close()


thread_send = threading.Thread(target=send_msg)
thread_send.start()

thread_receive = threading.Thread(target=recevice_msg)
thread_receive.start()
