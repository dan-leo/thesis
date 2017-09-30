import asynchat
import asyncore
import socket
import threading
 
class ChatClient(asynchat.async_chat):
 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator('\n')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        pass
 
    def found_terminator(self):
        pass

class ChatListener(asynchat.async_chat):
 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator('\n')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        self.buffer.append(data)
 
    def found_terminator(self):
        msg = ''.join(self.buffer)
        print 'Received:', msg
        self.buffer = []

#client = ChatClient('localhost', 5050)
listener = ChatListener('localhost', 5050)
 
comm = threading.Thread(target=asyncore.loop)
# comm.daemon = True
comm.start()
 
while True:
    msg = raw_input('> ')
    listener.push(msg + '\n')
