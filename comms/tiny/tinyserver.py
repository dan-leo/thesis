import socket, os, threading
from threading import Thread
from time import sleep, time

clients = set()
clients_lock = threading.Lock()
camera_mode = False
cameras_triggered = 0
time_now = 0


def listener(_client, _address):
    global camera_mode, cameras_triggered
    print("Accepted connection from: ", _address)
    cameras_triggered += 1
    with clients_lock:
        clients.add(_client)
    try:
        while True:
            data = _client.recv(32)
            print(repr(data))
            if not data:
                break
            if "CAMERA_MODE_ENABLED" in data:
                camera_mode = True
                for c in clients:
                    c.sendall("ACK")
            if "CAMERA_MODE_DISABLED" in data:
                camera_mode = False
                for c in clients:
                    c.sendall("ACK")
            if "CAMERA_COMPLETE":
                cameras_triggered += 1
    except Exception as e:
        print(e)
    finally:
        with clients_lock:
            clients.remove(_client)
            _client.close()


def camera_process():
    global camera_mode, cameras_triggered, clients, time_now
    print("Trigger thread ready.")
    while True:
        if camera_mode and cameras_triggered >= len(clients) > 0:
            cameras_triggered = 0
            with clients_lock:
                print("Sending trigger to " + repr(len(clients)) + " clients; last " + repr(time() - time_now) + ".")
                time_now = time()
                for c in clients:
                    c.sendall("TRIGGER_NOW")
        sleep(0.001)

t = Thread(target=camera_process)
t.daemon = True
t.start()

host = ''
port = 10017

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(3)
th = []

try:
    while True:
        print("Server is listening for connections...")
        client, address = s.accept()
        print ("hi")
        t = Thread(target=listener, args=(client, address))
        t.daemon = True
        th.append(t.start())
except KeyboardInterrupt as e:
    print(e)

