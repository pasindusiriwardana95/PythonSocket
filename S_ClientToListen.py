import socket

# This is a simple client

s = socket.socket()

PORT = 12345

s.connect(('127.0.0.1',PORT))

# receive data from the server
print(s.recv(1024))

s.close()
