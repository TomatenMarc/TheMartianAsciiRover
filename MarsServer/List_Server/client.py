import socket

host = input('>>host: ')
port = int(input('>>port: '))

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[+] Waiting for input ...')
    s.connect((host, port))
    msg = s.recv(1024).decode('ascii')
    s.close()
    print('>> %s' % msg)
