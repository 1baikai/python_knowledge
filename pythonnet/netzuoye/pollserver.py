from socket import *
from select import *

s =socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

p =poll()

fmap={s.fileno():s}

p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fmap[fd].accept()
            print("connect from ",addr)
            p.register(c,POLLIN | POLLERR)
            fmap[c.fileno()] = c
        elif event & POLLIN:
            data = fmap[fd].recv(1024)
            if not data :
                p.unregister(fd)
                fmap[fd].close()
                del fmap[fd]
            else:
                print(data.decode())
                fmap[fd].send(b'recv')