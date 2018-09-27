from threading import Thread
from time import sleep,ctime


class MyThread(Thread):
    def __init__(self,target,name ='t',args=(),kwargs={}):
        super().__init__()
        self.target = target
        self.args =args
        self.kwargs =kwargs
        self.name = name
    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(2):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)





t = MyThread(target = player,args=('凉凉',),kwargs = {"sec":2})
t.start()
t.join()