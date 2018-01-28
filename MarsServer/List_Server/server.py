# server.py
import socket
import time

host = "0.0.0.0"
port = 6000
# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    x = input("Text: ")
    clientsocket.send(x.encode())
    clientsocket.close()
