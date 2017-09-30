# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50011              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s.connect((HOST, PORT))
#s.sendall('Hello, world\n')
#data = s.recv(1024)
#s.close()
#print 'Received', repr(data)

try:
    while 1:
        s.sendall('Hello, world\n')
        data = s.recv(1024)
        #if not data: break
        print 'Received', repr(data)
except Exception as e:
    print e
    s.close()
