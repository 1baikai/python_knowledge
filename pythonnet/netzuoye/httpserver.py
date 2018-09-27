from socket import *

def  head(c):
    data = c.recv(4096)
    datalines= data.splitlines()
    for d in datalines:
        print(d.decode())
    try:
        f = open("index.html")
    except IOError:
        response = "HTTP/1.1 404  not found\r\n"
        response+="\r\n"
        response+="====="
    else:
        response ="HTTP/1.1 200   OK\r\n"
        response+="\r\n"
        response+=f.read()
    finally:
        c.send(response.encode())

def main():
    s= socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    HOST = '0.0.0.0'
    POST = 8888
    ADDR =(HOST,POST)
    s.bind(ADDR)
    s.listen(5)
    while True:
        c,addr = s.accept()
        head(c)
        c.close()
    s.close()

if __name__  == "__main__":
    main()