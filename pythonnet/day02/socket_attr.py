from socket import *

s=socket()
#设置端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取套接字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
#获取套接字地址族类型
print(s.family)
#获取套接字类型
print(s.type)
#绑定ｉp
s.bind(('176.233.4.99',8888))
#获取套接字的绑定地址ip
print(s.getsockname())
#获取套接字文件描述符
print(s.fileno())

s.listen(5)
while True:
    c,addr=s.accept()#c是客户端套接字
    print(c.getpeername())
    c.recv(1024)