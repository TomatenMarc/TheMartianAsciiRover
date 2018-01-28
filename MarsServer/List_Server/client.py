# client.py
import socket

host = "0.0.0.0"
port = 6000

while True:
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Waiting for input")
    # connection to hostname on the port.
    s.connect((host, port))
    # Receive no more than 1024 bytes
    tm = s.recv(1024)
    s.close()
    print(">> %s" % tm.decode('ascii'))
