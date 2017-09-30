import socket
from threading import Thread
from time import sleep

# clients = set()
# clients_lock = threading.Lock()
sock = socket.socket()
ack = False


def process_data():
    global sock, ack
    connected = False
    while not connected:
        try:
            sock.connect(('localhost', 10017))
            connected = True
        except Exception as e:
            print(e)
    try:
        while True:
            data = sock.recv(32)
            # print("data: " + repr(data))
            if "KEEP_ALIVE" in data:
                sock.sendall("KEEP_ALIVE")
            if "ACK" in data:
                ack = True
            if "TRIGGER_NOW" in data:
                sleep(0.4)
                sock.sendall("CAMERA_COMPLETE")
    except Exception as e:
        print(e)
    finally:
        sock.close()

Thread(target=process_data).start()

while True:
    sleep(1)
    if not ack:
        sock.sendall("CAMERA_MODE_ENABLED")
# process_data()
