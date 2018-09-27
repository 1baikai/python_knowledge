# broadcast_sent.py
from socket import *
from time import sleep


#设置目标地址

dest = ('176.233.4.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(3)
    s.sendto("你是谁？".encode(),dest)

s.close()
