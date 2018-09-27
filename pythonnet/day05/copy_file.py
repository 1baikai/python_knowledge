import os
from multiprocessing import process

file='./qqq.png'
size = os.path.getsize(file)

def copy1(file):
    f = open(file,'rb')
    n = size //2
    fw= open('1.png','wb')
    while True:
        if n <1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -=1024
    f.close()
    fw.close()

def copy2():
    f = open(filename,'rb')
    fw = open('2.png','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)
p1.start()
p2.start()
p1.join()
p2.join()