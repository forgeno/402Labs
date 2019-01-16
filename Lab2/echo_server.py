import socket
import time

HOST = ""
PORT =  8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    c, addr = s.accept()
    print('Connection from: ' + str(addr))
    while True:
        data = c.recv(1024)
        print(data)
        if not data:
            break
        print('from connected user: ' + str(data))
        data = str(data).upper()
        print('sending: ' + str(data))
        c.sendall(data)
    c.close()