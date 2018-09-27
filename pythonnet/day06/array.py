from multiprocessing import Process,Array

import time

#创建共享内存，出事放入列表
shm = Array('i',[1,2,3,4,5,6,7])
# 创建共享空间，开辟５个整形空间
# shm = Array('i',5)

#存入字符串,要求是ｂｙｔｅｓ格式
# shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
        shm[0]=21321

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i)
print(shm.value)