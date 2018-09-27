import multiprocessing as mp 
from time import sleep
import os





def write(file,x):
    fw = open(file,'wb')
    fw.write(x)
    fw.close()

def th1(file,x):
    write(file,x)
def th2(file,x):
    write(file,x)

def main():
    file = input("请输入文件名:")
    file1 = input("请输入上部分文件名:")
    # file2 = input("请输入下部分文件名:")
    fr = open(file,'rb')
    s = fr.read()
    fr.close()
    a=s[0:int(len(s)//2+1)]
    b=s[int(len(s)//2+1):]
    p = mp.Process(target = th2(file1,b))
    p.start()
    th1(file1,a)
    p.join()

if __name__ == "__main__":
    main()