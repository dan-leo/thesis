import socket
# import threading
from threading import Thread, Lock

print "Welcome to socket server"
s = socket.socket()         # Create a socket object
print s
host = socket.gethostname() # Get local machine name
print host
port = 12345                # Reserve a port for your service.
print s.bind((host, port))        # Bind to the port
print s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
print c

def recvfun():
    for i in range(5):
        print c.recv(1024)
    return

def sendfun():
    for i in range(5):
        c.send(raw_input())
    return

try:
    Thread(target = recvfun, args = []).start()
    Thread(target = sendfun, args = []).start()
except Exception,errtxt:
    print errtxt
    c.close()                   # Close the connection
