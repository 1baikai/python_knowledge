#!/usr/bin/env python3
#指明编译器的位置
from socket import *
import sys

if len(sys.argv)<3:
    print('''
        argv is error!
        run as
        python3 upd_client.py 127.0.0.1 8888
        ''')
    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#消息收发
while True:
    data = input("消息：")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务端收到：",data.decode())
sockfd.close()
