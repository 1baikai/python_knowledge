import socket 
import time

addr = ("127.0.0.1",8888)

s= socket.socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while Ture:
    time.sleep()
    s.sendto("asdasfasfdasdasd".encode(),addr)
s.close()