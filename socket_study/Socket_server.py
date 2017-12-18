# coding=utf-8

import socket, time
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9999))

#  Enable a server to accept connections
server_socket.listen(10)

print('wating for connection')


def tcplink(con, addr):
    print('new connection from %s:%s' % addr)
    con.send(b'welcome coming')
    while True:
        data = con.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        con.send(('hello %s' % data.decode('utf-8')).encode('utf-8'))
    con.close()
    print('connection from %s:%s closed' % addr)


while True:
    # con 是一个socke对象  addr 是一个元组
    con, addr = server_socket.accept()
    print(con)
    print(addr)
    t = threading.Thread(target=tcplink, args=(con, addr))
    t.start()
