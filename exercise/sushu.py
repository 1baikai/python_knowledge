  # 2. 写一个实现迭代器协议的类,让此类可以生成从b 开始的n个素数
class Prime:
    def __init__(self, b, n):
        self.begin=b
        self.count=n
    def __iter__(self):
        self.L=[]
        while self.count!=0:
            if self.begin < 2:  # 跳过小于2的数
                pass
            for i in range(2, self.begin):
                if self.begin % i == 0:
                    break
            else:
                self.L.append(self.begin)
                    
                self.count-=1
            self.begin+=1
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


        
           
L = [x for x in Prime(10, 4)]
print(L)  # L = [11, 13, 17, 19]
