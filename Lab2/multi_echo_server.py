import socket
import time

HOST = ""
PORT =  8001 
BUFFER_SIZE = 1024    
from multiprocessing import Process

def handle_echo(addr, c):
    print('Connection from: ' + str(addr))
    while True:
        data = c.recv(BUFFER_SIZE)
        #print(data)
        if not data:
            break
        #print('from connected user: ' + str(data))
        #data = str(data).upper()
        #print('sending: ' + str(data))
        c.sendall(data)
        c.shutdown(socket.SHUT_RDWR)
def main():   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(2)
    while True:
        c, addr = s.accept()
        p = Process(target = handle_echo(addr, c), args=(addr, c))
        p.daemon = True
        p.start()
        print("Starting process: ",p)
    
if (__name__ == "__main__"):
    main()