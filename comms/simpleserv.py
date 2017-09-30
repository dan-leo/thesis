
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    # def __init__(self, factory):
    #     self.factory = factory

    # def connectionMade(self):
    #     self.factory.numProtocols += 1
    #     self.transport.write("Welcome! There are currently %d open connections.\n" % (self.factory.numProtocols,))
    
    def dataReceived(self, data):
        """As soon as any data is received, write it back."""
        self.transport.write(data)

    def connectionLost(self, reason):
        print("connection lost")


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
