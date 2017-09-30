
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
An example client. Run simpleserv.py first before running this.
"""
from __future__ import print_function

from twisted.internet import reactor, protocol, error, threads
import threading
from time import sleep


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        self.transport.write("hello, world!")
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        # sleep(1)
        # self.transport.loseConnection()
    
    def connectionLost(self, reason):
        self.transport.loseConnection()
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        try: reactor.stop()
        except error.ReactorNotRunning, e: print(e)
    
    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        try: reactor.stop()
        except error.ReactorNotRunning, e: print(e)

def aSillyBlockingMethodOne(x):
    import time
    while True: 
        time.sleep(1)
        print(x)

def aSillyBlockingMethodTwo(x):
    import time
    while True: 
        time.sleep(0.4)
        print(x)

# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    # run both methods sequentially in a thread
    commands = [(aSillyBlockingMethodOne, ["Calling First"], {})]
    commands.append((aSillyBlockingMethodTwo, ["And the second"], {}))
    threads.callMultipleInThread(commands)
    # reactor.callInThread(aSillyBlockingMethodOne, "2 seconds have passed")
    reactor.run()
    # reactor.run(installSignalHandlers=0)
    print("RUNNING")

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
    # comm = threading.Thread(target=main)
    # comm.daemon = True
    # comm.start()
