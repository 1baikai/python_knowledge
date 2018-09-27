from socket import *
import os,sys
# from threading import *
from multiprocessing import Process
import signal

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handler(connfd):
    print("Connect from ",connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'Receive request')
    connfd.close()
    sys.exit(0)



s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEPORT,1)
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
    try:
        connfd,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception:
        traceback.print_exc()
        continue
    t = Process(target = handler,args=(connfd,))
    t.daemon=True
    t.start()
