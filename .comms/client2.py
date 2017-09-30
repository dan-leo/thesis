#!/usr/bin/python
import socket
import sys
import threading
 
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 9997)
sckt.connect(server_address)
 
 
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