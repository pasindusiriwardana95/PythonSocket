import socket

# This is a simple client

s = socket.socket()

PORT = 8000

HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)

s.connect((IP,PORT))

# receive data from the server
print(s.recv(4096))

s.close()
