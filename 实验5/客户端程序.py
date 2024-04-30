import socket

s = socket.socket()
host = socket.gethostname()
port = 12341
s.connect((host, port))
print(s.recv(1024).decode('utf_8', errors='strict'))
print(s.recv(1024).decode('utf_8', errors='strict'))
print(s.recv(1024).decode('utf_8', errors='strict'))
meg = '我是客户端'
s.send(meg.encode('utf-8',errors='ignore'))
s.close()
