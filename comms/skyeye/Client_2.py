import socket
import os
from threading import Thread
import threading

REQ = b'\x00'
SYN = b'\x01'
ACK = b'\x02'
SYN_ACK = b'\x03'
KEEPALIVE = b'\x04'
ID_1 = b'\x00\x00'
ID_2 = b'\x00\x01'
clients = set()
clients_lock = threading.Lock()

def process_data():
    sock = socket.socket()
    sock.connect(('localhost', 10016))
    while True:
        a = sock.recv(1024)
        if a == KEEPALIVE:
            sock.sendall(KEEPALIVE)
            # a = sock.recv(1024)

        if a == SYN:
            sock.sendall(ACK+ID_2)
            # a = sock.recv(1024)


Thread(process_data())
