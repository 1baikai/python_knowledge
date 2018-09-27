from signal import *
import time 

def handler(sig,frame):
    if sig == SIGALRM:

        print("接收到时钟信号")
    elif sig == SIGINT:
        print("就不结束")

a=alarm(5)

signal(SIGALRM,handler)

while True:
    print("waiting ....")

    time.sleep(2)