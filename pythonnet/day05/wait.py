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
    pid,status = os.wait()
    print(pid,status)#status是os＿exit()的256倍
    print(os.WEXITSTATUS(status))
    while True:
        pass
