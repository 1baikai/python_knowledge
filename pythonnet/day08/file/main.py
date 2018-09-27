from socket import *
import os,sys
import signal#避免僵尸进程
# import #自己写的类

HOST = ""
PORT = 8888
ADDR =(HOST,PORT)


def main():
    #连接客户端


    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    print("进程%d等待客户端连接"%os.getpid())
    #在父进程中忽略子进程状态改变，子进程退出自动由系统处理
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e :
            print("Error:",e)
            continue
        # 有客户端连接，为客户端创建新的进程处理请求
        pid = os.fork()
        if pid == 0:
            s.close()
            #显示界面
           
        #父进程或者创建失败都继续等待下一个客户端连接
        else:
            c.close()
            continue

if __name__ == "__main__":
    main()