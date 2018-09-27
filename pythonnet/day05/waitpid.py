import os
from time import sleep

pid = os.fork()

if pid<0:
    print("创建失败")
elif pid == 0:
    sleep(3)
    print("sun process exit",os.getpid())
    os._exit(5)
else:
    while True:
        sleep(1)
        #通过非阻塞的形式捕获子进程退出
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)#status是os＿exit()的256倍
        print(os.WEXITSTATUS(status))
        if pid!= 0:
            break
    while True:
        pass
