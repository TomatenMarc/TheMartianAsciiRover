import socket

host = input('>>host: ')
port = int(input('>>port: '))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(5)
try:
    while True:

        clientsocket, addr = serversocket.accept()
        print('[+] Got a connection from %s' % str(addr))
        msg = input('>>Text: ').encode('ascii')
        clientsocket.send(msg)

except (KeyboardInterrupt, SystemExit):
    clientsocket.close()
