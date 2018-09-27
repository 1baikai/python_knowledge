from multiprocessing import Process,Event
from time import sleep

def wait_event():
    print("想操作临界资源")
    # e.wait()
    print("开始操作",e.is_set())

    with open("file") as f:
        print(f.read())

def wait_event_timeout():
    print("y也想操作")
    
    # e.wait(2)
    if e.is_set():

        with open("file") as f:
            print(f.read())
    else:
        print("读取不了了")



e = Event()
p1 = Process(target = wait_event)
p1.start()
p2 = Process(target = wait_event_timeout)
p2.start()


print("主进程操作")

with open('file','w') as f:
    sleep(3)
    f.write("i love china")

e.set()
print("释放")
p1.join()
p2.join()