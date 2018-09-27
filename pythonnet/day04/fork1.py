# fork1.py

import os

pid = os.fork()

if pid<0:
    print("create process failed")
elif pid ==0:
    #获取当前进程的ＰＩＤ
    print("child get pid",os.getpid())
    #获取父进程的ＰＩＤ
    print("child get father pid",os.getppid())
else:
    print("father get child pid",os.getpid())
    print("father get pid",os.getpid())