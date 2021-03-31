import socket
import sys

# This is a simple server.
s = socket.socket()
print("Socket created succesfully!")

HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)

#reserve a port in my computer, this can be any port number
PORT = 8000


# 1.Binding to the port is up next
# 2.our IP address field for now is empty - this lets the server to listen to requests coming from other computers on the network
s.bind((IP,PORT))
print("Socket binded to %s" %PORT)

# listen(5) means that 5 connections are kept waiting if the server is busy and if the 6th socket tries to connect then the connection is refused.
s.listen(5)  
print("The socket is listening...")

data = 'Thanks for connecting!'
while True:
    #establsih connection with client
    c,addr = s.accept()
    print('Got connection from',addr)

    #send a note to the client
    c.send(data.encode())

    #close the connection with the client
    c.close()
