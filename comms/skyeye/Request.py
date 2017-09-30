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


sock = socket.socket()
sock.connect(('127.0.0.1', 10016))
while True:
    sock.sendall(REQ)
    time.sleep(5)