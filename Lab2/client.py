import socket

HOST = 'www.google.com'
PORT = 80
BUFFER_SIZE = 2048
returnData = ""

request = "GET / HTTP/1.0\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(request)
data = s.recv(BUFFER_SIZE)
while(len(data) != 0):
    returnData += data
    data = s.recv(BUFFER_SIZE)
print(returnData)