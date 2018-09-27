from socket import *
import sys
if len(sys,argv)<3:
    print("""
        argv is error
        """)

HOST = sys.argv[1]
POST =int(sys.argv[2])
ADDR = (HOST,POST)

s = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("消息")
    if not data:
        break
    s.sendto(data.encode(),ADDR)
    data,addr = s.recvfrom(1024)
    print(data.decode())
s.close()