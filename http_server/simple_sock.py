

# non-blocking sock server

import socket

sock = socket.socket()

sock.connect(('localhost',8889))
sock.setblocking(0)

while True:
    msg = input('>')
    try:
        sock.send(msg.encode('utf8'))
        text = sock.recv(1000).decode('utf8')
    except BlockingIOError:
        pass
    else:
        print(text)
