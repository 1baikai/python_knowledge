from time import sleep
from multiprocessing import Process

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("Process pid",p.pid)
        print("I'm working...")

# p = Process(target = worker,args = (2,'zhang'))
p = Process(target = worker,args = (2,),kwargs={'name':'divl'},name='worker')


p.start()

print("Process name",p.name) #进程名称
print("Process pid",p.ppid)#获取进程PID
print("Process is alive:",p.is_alive()) #进程ａｌｉｖｅ情况

p.join(1)

print("=====================") 