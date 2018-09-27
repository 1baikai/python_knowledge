# exercise_serve.py
from socket import *

sock1 = socket(AF_INET,SOCK_STREAM)

sock1.bind(('0.0.0.0',8889))

sock1.listen(5)

while True:
    print("等待连接.......")
    c,addr = sock1.accept()
    while True:
        try:
            file = input("要保存的文件名:")
            fw = open(file,'wb')
            data = c.recv(600000)
            fw.write(data)
            fw.close()
            print("保存成功")
        except OSError:
            print("保存失败")


        n = c.send(b'Receive your message')
    c.close()


sock1.close()