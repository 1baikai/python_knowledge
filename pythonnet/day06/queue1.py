from multiprocessing import Queue

from time import sleep

#创建队列
q = Queue(3)
q.put(1)
sleep(0.5)
print(q.empty())

q.put(2)
print(q.full())
q.put(3)
print(q.qsize())
print(q.full())
# q.put(4,True,3)

print(q.get())
print(q.get())
print(q.get())
