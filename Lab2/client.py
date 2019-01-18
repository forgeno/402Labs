#!/usr/bin/env python3

import socket

HOST = 'www.google.com'
PORT = 80
payload = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(HOST)
BUFFER_SIZE = 2048
returnData = ""

def get_request(addr):
    (family, sockettype, proto, canonname, sockaddr) = addr
    try:
        s = socket.socket(family, sockettype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        data = s.recv(BUFFER_SIZE)
        print(full_data)
        
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
       
    addr_info = socket.getaddrinfo(HOST, PORT)
    for addr in addr_info:
        (family, sockettype, proto, canonname, sockaddr) = addr
        if(family == socket.AF_INET and  sockettype == socket.SOCK_STREAM):
            print(addr)
            get_request(addr)


if (__name__ == "__main__"):
    main()