# poll_server.py
from socket import *
from select import *

#创建套间字作为我们关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p = poll()
#fileno----->IO对象的字典
fdmap = {s.fileno():s}
#注册关注的io
p.register(s,POLLIN | POLLERR)

while True:
    #进行ＩＯ监控
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("connect from",addr)
            p.register(c,POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'recrive')


