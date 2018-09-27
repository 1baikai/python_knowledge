# exerise_client.py

from socket import *

sock2 = socket(AF_INET,SOCK_STREAM)
server_addr=("127.0.0.1",8889)
sock2.connect(server_addr)

while True:
    try:
        file=input("你要发送的文件:")
        fr = open(file,'rb')
        data = fr.read()
        sock2.send(data)
        fr.close()
        print("发送成功")
        data = sock2.recv(1024)
        print("接受到",data.decode())
    except OSError:
        print("文件打开失败")
sock2.close()
