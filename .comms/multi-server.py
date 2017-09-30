import threading
import time
import sys
from datetime import datetime
from socket import *


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        serverSide()
        # Free lock to release next thread
        # threadLock.release()

class myThread1 (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        clientSide()
        # Free lock to release next thread
        # threadLock.release()



def serverSide():
    serverPort = 44000
    serverIP = '127.0.0.1'
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind((serverIP,serverPort))
    print ("SERVER HERE!\nThe server is ready to receive")
    while 1:
        print ("while 1")
        message, clientAddress = serverSocket.recvfrom(2048)
        print (message, clientAddress)
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage, clientAddress)


def clientSide():
    serverIP = "127.0.0.1"
    serverPort = 44000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input("CLIENT HERE!\nInput lowercase sentence:")

    clientSocket.sendto(message.encode(),(serverIP, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("received", modifiedMessage) # print the received message

    clientSocket.close() # Close the socket

# threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread1(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")