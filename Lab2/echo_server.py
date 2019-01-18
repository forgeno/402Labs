import socket
import time

HOST = ""
PORT =  8001 
BUFFER_SIZE = 1024    

def main():   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        c, addr = s.accept()
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
        c.close()     
       
if (__name__ == "__main__"):
    main()