import threading
import time

def func():
    for i in range(5):
        time.sleep(2)
        print("asd")

t = threading.Thread(target = func)

t.start()
for i in range(5):
    time.sleep(1.55)
    print("vdfg")

t.join()