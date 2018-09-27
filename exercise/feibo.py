  # 3. 写一个类Fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成斐波那契数列
         # 1 1 2 3 5 8 13 ....
class Fibonacci:
    def __init__(self, n):
        self.end=n
    def __iter__(self):
        self.L=[]
        self.a=0
        self.b=1
        while  self.b<=self.end:
        	self.L.append(self.b)
        	self.a,self.b=self.b,self.a+self.b
        return MyListIterator(self.L) 
class MyListIterator:
    '''此类用来描述能够访问MyList类型的对象的迭代器'''
    def __init__(self, lst):
        self.data_lst = lst
        self.cur_index = 0   # 迭代器访问的起始位置

    def __next__(self):
        '''此方法用来实现迭代器协议'''
      
        if self.cur_index >= len(self.data_lst):
            raise StopIteration

        r = self.data_lst[self.cur_index]
        self.cur_index += 1
        return r
for x in Fibonacci(10):
    print(x)  # 打印 1 1 2 3 5 8 ...