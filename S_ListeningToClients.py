import socket
import sys

# This is a simple server.
s = socket.socket()
print("Sockt created succesfully!")

#reserve a port in my computer, this can be any port number
PORT = 12345

# 1.Binding to the port is up next
# 2.our IP address field for now is empty - this lets the server to listen to requests coming from other computers on the network
s.bind(('',PORT))
print("Socket binded to %s" %PORT)

# listen(5) means that 5 connections are kept waiting if the server is busy and if the 6th socket tries to connect then the connection is refused.
s.listen(5)  
print("The socket is listening...")

while True:
    #establsih connection with client
    c,addr = s.accept()
    print('Got connection from',addr)

    #send a note to the client
    c.send('Thanks for connecting!')

    #close the connection with the client
    c.close()
