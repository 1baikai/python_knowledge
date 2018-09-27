import gevent
from time import sleep

def foo(a,b):
    print("a=%d,b=%d"%(a,b))
    gevent.sleep(2)
    print("r unning foo again")
def bar():
    print("running in bar")
    gevent.sleep(3)
    print("running bar again")

f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)

print("================")
gevent.joinall([f,g])
print("=_____+_+_+_+_+_+=")