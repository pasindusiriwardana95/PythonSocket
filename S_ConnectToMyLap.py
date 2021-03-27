import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("socket creation failed with error %s" %(err))

#defualt port for socket
PORT = 80

try:
    host_ip = socket.gethostbyname('DESKTOP-0JIJIKS')
    #DESKTOP-0JIJIKS
    #DS-K1T8003EF
except socket.gaierror:
    # this means could not resolve the host
    print("There was an error resolving the host")
    sys.exit()

#connecting to the server
    s.connect((host_ip, port))

print("The socket has successfully connected to the Host!")
print("The host IP Address: %s" %host_ip)
