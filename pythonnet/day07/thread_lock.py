import threading

a=b=0

lock = threading.Lock()

def values():
    while True:
        lock.acquire()
        if a !=b:
            print("a = %d,b=%d"%(a,b))
        lock.release()

t =threading.Thread(target =values)

t.start()

while True:
    with lock:
        a+=1
        b+=1

t.join()
