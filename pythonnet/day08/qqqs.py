'''
ftp文件服务器
'''
from socket import *
import os
import sys
import time 
import signal

#文件库路径

FILE_PATH= "/home/tarena/aid1807/python/pythonnet/ftp/"
HOST = '0.0.0.0'
POST = 8000
ADDR = (HOST,POST)

#将文件服务器功能写在类中
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                files =files +file + '#'
        self.connfd.sendall(files.encode())
    def do_down(self):


#创建套接字，接受客户端连接，创建新的进程
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    #处理子进程退出
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("listen the port 8000...")

    while True:
        try :
            connfd,addr = sockfd.accept()
        except  KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常",e)
            continue
        print("已连接客户端")

        #创建子进程
        pid = os.fork()
        if pid ==0:
            sockfd.close()
            ftp = FtpServer(connfd)
            #判断客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data:
                    connfd.close()
                    sys.exit("客户端退出")
                elif data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'D':
                    ftp.down()

            
        else:
            connfd.close()
            continue



if __name__ =="__main__":
    main()