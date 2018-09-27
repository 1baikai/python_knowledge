#encoding:utf-8
from socket import *
import os,sys
from multiprocessing import Process,Event

def do_chat(s,user,name,text):
    msg = "\n%s说:%s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
def do_quit(s,uaer,name):
    msg = '\n'+name + "退出了聊天室"
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]


def do_child():
    # pass
    while True:
        msg = input("管理说")
        msg = 'C 管理员 ' +msg
        s.sendto(msg.encode(),addr)



def do_parent(s):
    user={}
    while True:
        data,addr = s.recvfrom(1024)
        msglist=data.decode().split(' ')
        if msglist[0]=='L':
            do_login(s,user,msglist[1],addr)
        elif msglist[0]=='C':
            do_chat(s,user,msglist[1],' '.join(msglist[2:]))
        elif msglist[0]=="Q":
            do_quit(s,user,msglist[1])
def do_login(s,user,name,addr):
    if name in user:
        s.sendto("名字重复".encode(),addr)
    else:
        s.sendto(b'ok',addr)
        for i in user:
            s.sendto(("欢迎%s进入聊天室"%name).encode(),user[i])
        user[name]=addr



def main():
    ADDR= ("0.0.0.0",8888)
    s =socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEPORT,1)
    s.bind(ADDR)
    # e = Event()
    p = Process(target = do_child)
    p.daemon=True
    p.start()

    do_parent(s)

if __name__ =="__main__":
    main()

