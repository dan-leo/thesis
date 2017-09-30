import socket
# import threading
from threading import Thread, Lock

# def recvfun():
#     for i in range(5):
#         print c.recv(1024)
#     return

# def sendfun():
#     for i in range(5):
#         c.send(raw_input())
#     return

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
# host = "localhost"
# host = socket.gethostname() # Get local machine name
s.connect((host, port))

# try:
#     Thread(target = recvfun, args = []).start()
#     Thread(target = sendfun, args = []).start()
# except Exception,errtxt:
#     print errtxt
#     s.close                     # Close the socket when done
