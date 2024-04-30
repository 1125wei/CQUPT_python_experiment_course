import socket

s = socket.socket()
host = socket.gethostname()
port = 12341
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("connection address:", addr)
    meg = '连接成功'
    c.send(meg.encode(encoding='utf_8', errors='strict'))
    meg = '欢迎你的到来'
    c.send(meg.encode(encoding='utf_8', errors='strict'))
    meg = '我是服务器'
    c.send(meg.encode(encoding='utf_8', errors='strict'))
    client = c.recv(1024)
    print(c.recv(1024).decode(encoding='utf_8', errors='strict'))
    c.close()
