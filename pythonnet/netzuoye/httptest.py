from socket import socket

s=socket()

s.bind(('0.0.0.0',8000))

s.listen(5)

while True:
    c,addr = s.accept()
    data = c.recv(4096)
    print("$$$$$$$$$$$$$$$$$$$$$")
    print(data)
    print("$$$$$$$$$$$$$$$$$$$$$")

    data = ''' HTTP/1.1 200 OK
    Content-Encoding:gzip
    Content-Type :text/html

    <h1>afdfsdfg</h1>
    '''
    c.send(data.encode())
    c.close()

s.close()