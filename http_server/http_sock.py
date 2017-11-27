
import socket
import time

def get(path):
    sock = socket.socket()
    sock.connect(('localhost',5000))
    request = 'GET {} HTTP/1.0\r\n\r\n'.format(path)
    print("sending request to:",request)
    sock.send(request.encode())
    print("sockno:",sock.fileno())

    buf = []
    while True:
        chunk_val = 5000
        total_chunks = 0
        chunk = sock.recv(chunk_val)
        if chunk:
            total_chunks += chunk_val
            print("downloading...total_chunks:",total_chunks)
            buf.append(chunk)
        else:
            body = b''.join(buf).decode()
            print(body)
            return

s = time.time()
get('/hello')
print(time.time()-s)
