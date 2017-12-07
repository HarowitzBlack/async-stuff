

# why do we need to import the DefaultSelector??? wtf??
# it's confusing initially, but everything will make sense :)
from selectors import DefaultSelector,EVENT_WRITE
import socket

# so at the core selector module is like a notebook
# you write down anything you want in it for future reference
# You can write stuff into it, read it or delete it.

# so we create a DefaultSelector() object. That's the notebook
selector = DefaultSelector()

sock = socket.socket()
# this is for async stuff
# instead of letting one way systematic requests, you can send concurrent
# requests
sock.setblocking(False)

try:
    sock.connect(('xkcd.com',80))
except BlockingIOError:
    # this error is thrown for no reason
    pass

def conn():
    # this func will be call later
    # so basically what it does is when this func is called, it deletes the record from
    # notebook. That is, when writing it down, a sockets id was used to register it. But now
    # we dont want it so we unregister it
    selector.unregister(sock.fileno())
    print("connected!")

# this registers a socket into the notebook and a function is passed
# which is to be executed when the socket is found in the notebook
# it doesnt make sense now, but it will.
# EVENT_WRITE is just a writing mode that allows us to save the socket
# into the notebook
selector.register(sock.fileno(),EVENT_WRITE,conn)
print("socket fileno:",sock.fileno())

def loop():
    while True:
        # when the socket was registered, it was added to a queue
        # so for every new url a new sock is created and added to the queue
        events = selector.select()
        print("registered socket:",events)
        # now to connect the socket we need a way to call the conn() function
        # But we cant do it just by calling conn(), because it'll just be the same
        # as systematic call. That's why we passed conn() when registering the socket.
        # The callback func ref resides inside the selector event
        for event_key,event_mask in events:
            print("event_key : ",event_key)
            print("event_mask: ",event_mask)
            # get the key
            callback = event_key.data
            # call the func
            callback()

loop()
