from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(213)
    gr2.switch()
def test2():
    print(65)
    gr1.switch()
    print(435)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()