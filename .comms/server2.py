#!/usr/bin/python
#A typical sequence of a socket connection.
#1 - Create socket
#2 - Bind the Socket to an IP and Port
#3 - Instruct the OS to accept connections as per specifications above.
#4 - Instruct the OS to recv-send data via the sockets.
#5 - Close Socket when it is not needed any longer.  
import socket
import sys
import threading
 
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 9997)
# sckt.connect(server_address)

print sckt.bind(server_address)        # Bind to the port
print sckt.listen(5)                 # Now wait for client connection.
c, addr = sckt.accept()     # Establish connection with client.
print 'Got connection from', addr
print c
 
 
def client_send():
        while True:
                message = raw_input("Text: ")
                sckt.send(message)
 
def client_recv():
        while True:
                reply = sckt.recv(1024)
                print "received", repr(reply)
 
threading.Thread(target = client_send).start() 
threading.Thread(target = client_recv).start()