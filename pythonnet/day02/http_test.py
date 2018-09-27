# http_test.py

from socket import *
#创建tcp套接字
s = socket()

s.bind(('0.0.0.0',8001))

s.listen(5)

while True:
    c,addr = s.accept()
    print("connect from",addr)
    data = c.recv(4096)
    print("*****************")
    print(data)#浏览器发来的http请求
    print("*****************")
    
    #组织响应内容
    data = '''HTTP/1.1 200 OK
    Conent-Encoding:gzip
    Conent-Type: text/html

    <h1>我爱你亲爱的祖国</h1>
    '''


    c.send(data.encode())
    c.close()

s.close()