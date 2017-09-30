from twisted.internet.threads import deferToThread as __deferToThread
from twisted.internet import reactor

def mmprint(s):
    print(s)

class TwistedRAWInput(object):
    def start(self,callable,terminator):
        self.callable=callable
        self.terminator=terminator
        self.startReceiving()
    def startReceiving(self,s=''):
        if s!=self.terminator:
            self.callable(s)
            __deferToThread(raw_input,':').addCallback(self.startReceiving)


tri = TwistedRAWInput()
reactor.callWhenRunning(tri.start,mmprint,'q')
reactor.run()
