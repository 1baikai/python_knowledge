from socket import *
import os,sys
from multiprocessing import Process,Event
import time


def do_send():
    # pass
    while True:
        
        text = input(">>>>>")
        if text.strip() =="quit":
            s.sendto(("Q "+name+text).encode(),addr)
            sys.exit("退出聊天室")
        msg = "C "+name+text
        s.sendto(msg.encode(),addr)
def do_recv(s):
    while True:
        data,addr= s.recvfrom(1024)
        if data.decode()=="EXIT":
            sys.exit(0)
        print(data.decode())

def main():

    if len(sys.argv)<3:
        print("输入地址和端口")

    HOST = sys.argv[1]
    POST = int(sys.argv[2])
    ADDR = (HOST,POST)
    s =socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("请输入姓名")
        msg = "L "+name
        s.sendto(msg.encode(),ADDR)

        data,addr =s.recvfrom(1024)
        if data.decode() =="ok":
            print("登录成功")
            break
        else:
            print(data.decode())
    
    p = Process(target=do_send)
    p.daemon=True
    p.start()
    do_recv(s)

if __name__=="__main__":
    main()
    
