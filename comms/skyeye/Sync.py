import socket
import time
from threading import Thread
import threading

REQ = b'\x00'
SYN = b'\x01'
ACK = b'\x02'
SYN_ACK = b'\x03'
KEEPALIVE = b'\x04'
clients = set()
clients_lock = threading.Lock()


def sync_data():
    sock = socket
    sock.socket.connect(['127.0.0.1', 10016])
    while True:
        time.sleep(0.5)
        sock.socket.sendall(KEEPALIVE)

Thread(sync_data())


