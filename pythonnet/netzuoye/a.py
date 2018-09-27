from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

while True:
    print("waiting.....")
    c,addr = s.accept()
    data = c.recv(4096)
    d = data.splitlines()
    for i in d:
        print(i.decode())
    try:
        f = open("index.html")
    except IOError:
        h = "HTTP/1.1 404 \r\n"
        h +="\r\n"
        h+="asdasfasfsdfagrdsgvadfgvadsfgvw"
    else:
        h ="HTTP/1.1 200 \r\n"
        h+="\r\n"
        h+=f.read()
    finally:
        c.send(h.encode())
    c.close()

s.close()

