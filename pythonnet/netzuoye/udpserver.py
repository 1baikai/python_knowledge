from socket import *

s= socket(AF_INET,SOCK_DGRAM)

server_addr = ('0.0.0.0',8888)

s.bind(server_addr)

while True:
    data,addr = s.recvfrom(1024)
    print(data.decode())
    s.sendto("接收到您的消息".encode(),addr)

s.close()