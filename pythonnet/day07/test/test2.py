from test import *
import threading
import time

t=time.time()
counts=[]
for x in range(10):
    th = threading.Thread(target = count,args=(1,1))
    counts.append(th)
    th.start()

for i in counts:
    i.join()

print("thread cpu",time.time()-t)
