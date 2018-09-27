from  multiprocessing import Pool
from time import sleep

def work(msg):
    sleep(2)
    print(msg)

pool = Pool(processes =4)

for i in range(10):
    msg = "hello%d"%i
    pool.apply_async(func =work,args=(msg,))
pool.close()
pool.join()

