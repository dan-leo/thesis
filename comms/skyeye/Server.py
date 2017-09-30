import socket
import os
from threading import Thread
import threading

# run server, then Client_1, then Requester. Requester starts to check the Client_1 connection and send commands. 
# Then you run Client_2, they sync and are ready to work together.

REQ = b'\x00'
SYN = b'\x01'
ACK = b'\x02'
SYN_ACK = b'\x03'
KEEPALIVE = b'\x04'
# different ID's for clients to tell them from each other.
# In analog transmissions are represented with different frequency tones
ID_1 = b'\x00\x00'
ID_2 = b'\x00\x01'
clients = set()
clients_lock = threading.Lock()

def listener(client, address):
    # global variable to store transmitted data, so every thread checks the only variable
    global data
    global LASTDATA
    # list of last 3 commands, that should match our pattern (first answered, second answered, in one request session),
    # in analog transmissions represented by tone beat of certain length
    LASTDATA = []
    print("Accepted connection from: ", address)
    with clients_lock:
        clients.add(client)
    try:
        while True:
            data = client.recv(1024)
            print(repr(data))
            if len(LASTDATA) > 3:
                # here we create an array of incoming data to server.
                # It should have all 3 elems (request, answer1 and answer2 to proceed)
                LASTDATA = []
            LASTDATA.append(data)
            if not data:
                break
            if data == KEEPALIVE:
                c.sendall(KEEPALIVE)
            if data == REQ:
                with clients_lock:
                    for c in clients:
                        c.sendall(SYN)
            # if answered only first client and request is transmitted
            if ACK+ID_1 in LASTDATA and REQ in LASTDATA:
                print(repr(data) + ' client 1 responded')
                print("SkyEyeOne reporting ready")
                with clients_lock:
                    for c in clients:
                        c.sendall(SYN)

            # if answered only second client and request is transmitted
            if ACK+ID_2 in LASTDATA and REQ in LASTDATA:
                print(repr(data) + ' client 2 responded')
                print("SkyEyeTwo reporting ready")
                with clients_lock:
                    for c in clients:
                        c.sendall(SYN)

            # if answered both and request is still transmitted
            if ACK+ID_1 in LASTDATA and REQ in LASTDATA and ACK+ID_2 in LASTDATA:
                with clients_lock:
                    for c in clients:
                        c.sendall(SYN_ACK)
                        print("Clients synced")
                        print("SkyEyes data transmission started")
    finally:
        with clients_lock:
            clients.remove(client)
            client.close()

host = 'localhost'
port = 10016

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
th = []

while True:
    print("Server is listening for connections...")
    client, address = s.accept()
    th.append(Thread(target=listener, args=(client, address)).start())

