from multiprocessing import Process
import signal
import os
import time

def func(sig,frame):
    if sig==SIGTSTP:
        a=os.getpid()
        os.kill(a,signal.SIGUSR1)
    elif sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("车速有点快，")

def shou():
    time.sleep(2)
    #判断接受的信号x
    signal.signal(signal.SIGTSTP,signal.SIG_IGN)
    if x == SIGINT:
        f = os.getppid()
        os.kill(f,signal.SIGUSR1)
    elif x == SIGQUIT:
        f = os.getppid()
        os.kill(f,signal.SIGUSR2)
    elif x== SIGUSR1:
        print("到站了，请下车")

p = Process(target = shou)





while True:
    signal.signal(signal.SIGTSTP,func)
    
    p.start()
    print("等待XINAHO.....")
    p.join()
