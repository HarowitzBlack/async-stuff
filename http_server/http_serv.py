
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('',8879))
sock.listen(1)

print('http serv started...')
while True:
    conn,addr = sock.accept()
    req = conn.recv(1024)
    print("\n",req.decode())

    http_resp = 'HTTP/1.1 200 OK \r\n\r\n Hello'
    conn.sendall(http_resp.encode('utf8'))
    conn.close()
