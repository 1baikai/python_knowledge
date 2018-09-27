from socket import *
import sys
import time

#基本文件操作功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')#发送请求
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split("#")
            for file in files:
                print(file)
            print("文件列表展示完毕")
        else:
            #由服务器发送失败原因
            print(data)

    def do_down(self,file):
        self.sockfd.send(b'D')
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            self.sockfd.send(file.encode())
            fw = open(file,'wb')
            while True:
                data1 = self.sockfd.recv(4096)
                if not data1:
                    break
                fw.write(data1)
            fw.close()


#网络连接
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)#文件服务器地址
    

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except:
        print("连接服务器失败")
        return
    ftp = FtpClient(sockfd)#功能类对象
    while True:
        print('***********************************************')
        print('*'+'1'+')查看文件库中普通文件'+'*')
        print('*'+'2'+')下载文件库文件到本地'+'*')
        print('*'+'3'+')上传文件到文件库'+'*')
        print('*'+'4'+')退出'+'*')
        print('***********************************************')

        cmd = input("请输入命令>>")
        if cmd.strip() == '1':
            ftp.do_list()
        elif cmd.strip()== "2":
            file = input("请输入要下载的文件：")
            ftp.do_down(file)

if __name__ == "__main__":
    main()