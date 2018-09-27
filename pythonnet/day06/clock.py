from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()

    def run(self):
        for i in range(5):
            print("The time is {}".format(time.ctime()))
            time.sleep(self.value)

p = ClockProcess(2)


p.start()

p.join()