import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("connection address:", addr)
    meg = '连接成功'
    conn.send(meg.encode(encoding='utf-8', errors='strict'))
    meg = '欢迎你的到来'
    conn.send(meg.encode(encoding='utf-8', errors='strict'))
    meg = '我是服务器'
    conn.send(meg.encode(encoding='utf-8', errors='strict'))
    print(conn.recv(1024).decode(encoding='utf', errors='strict'))
    conn.close()
