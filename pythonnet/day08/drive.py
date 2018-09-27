from multiprocessing import Process
import os
from signal import *
import time

def saler_hander(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("车站到了，请下车")
        os._exit(0)

def driver_hander(sig,frame):
    if sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("车速太快了，这不是去幼儿园的车...")
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)


#子进程为售票员
def saler():
    signal(SIGINT,saler_hander)
    signal(SIGQUIT,saler_hander)
    signal(SIGUSR1,saler_hander)
    signal(SIGTSTP,SIG_IGN)
    while True:
        time.sleep(2)
        print("waiting...")


p = Process(target = saler)

p.start()
signal(SIGUSR1,driver_hander)
signal(SIGINT,SIG_IGN)
signal(SIGUSR2,driver_hander)
signal(SIGQUIT,SIG_IGN)
signal(SIGTSTP,driver_hander)
p.join()