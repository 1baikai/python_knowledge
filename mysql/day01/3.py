# class Shape:
#     def draw(self):
#         print("Shape的draw()被调用")

# class Point(Shape):
#     def draw(self):
#         print("正在画一个点")

# class Circle(Point):
#     def draw(self):
#         print("正在画一个　")

# def my_draw(s):
#     s.draw()

# s1=Circle()
# s2=Point()
# my_draw(s1)
# my_draw(s2)

# class Peasant:
#     def farm(self,plant):
#         print("正在种植",plant)


# class Worker:
#     def work(self,that):
#         print("正在制造",that)


# class MigrantWorker(Peasant,Worker):
#     pass


# person=MigrantWorker()
# person.farm("水稻")
# person.work("汽车")
# print(MigrantWorker.__mro__)


# class MyList:
#     def __init__(self,iterable=()):
#         self.data=[x for x in iterable]

#     def  __repr__(self):
#         return 'MyList(%s)'%self.data
#     def __len__(self):
#         return len(self.data)
#     def __abs__(self):
#         L=[]
#         for i in self.data:
#             L.append(abs(i))
#         return MyList(L)


# myl=MyList([1,-2,3,-4])
# print(myl)
# print(len(myl))
# print(abs(myl))

# class MyNumber:
#     def __init__(self,val):
#         self.data=val 
#     def  __repr__(self):
#         return 'MyList(%s)'%self.data
#     def __int__(self):
#         return　int(self.data)
#     def __float__(self):
#         return　float(self.data)

# n1=MyNumber
# n=int(n1)
# print(n)

# f=float(n1)
# print(f)

# c= complex(n1)  ##如果没有n1.__complex__()时会调用n1.__float__() 
# print(c)  #

# class Mynumber:
#     def __init__(self,v):
#         self.data=v
#     def __repr__(self):
#         return 'Mynumber(%d)'%self.data
#     def __add__(self,other):
#         v=self.data +other.data
#         return Mynumber(v)
#     def __sub__(self,rhs):
#         return Mynumber(self.data-rhs.data)

# n1=Mynumber(100)
# n2=Mynumber(200)
# n3=n1+n2
# print(n3)
# n4=n3-n2
# print(n4)

# class MyList:
#     def __init__(self,iterable=()):
#         self.data=list(iterable)
#     def  __repr__(self):
#         return 'MyList(%s)'%self.data
#     def __add__(self,rhs):
#         return MyList(self.data+rhs.data)
#         # v=[]
#         # for i in self.data:
#         #     v.append(i)
#         # for x in other.data:
#         #     v.append(x)
#         # return MyList(v)
#     def __mul__(self,rhs):
#         return MyList(self.data*rhs)
#         # L=[]
#         # while rhs !=0:
#         #     for i in self.data:
#         #         L.append(i)
#         #     rhs-=1
#         # return MyList(L)
# L1=MyList([1,2,3])
# L2=MyList([4,5,6])
# L3=L1+L2
# print(L3)
# L4=L2+L1
# print(L4)
# L5=L1*5
# print(L5)

# def __delitem(self,i):
#     self.__data.pop[i]=v

# class Student:
#     def __init__(self,s):
#         self.__score=s

#     def setScore(self,s):
#         if 0<=s<=100:
#             self.__score=s


# s=Student(50)

class OrderSet:
    def __init__(self,it=None):
        if it is None:
            self.data = []
        elif it:
            self.v = [x for x in it]
    
    def  __repr__(self):
        return 'OrderSet(%r)'%self.v
    def __and__(self,other):
        # self.x=[]
        # for i in self.v:
        #     if i in other.v:
        #         self.x.append(i)
        # return OrderSet(self.x)
        return OrderSet(x for x in self.v if x in other.v)

    def __or__(self,other):
        self.x=[]
        for i in self.v:
            if i not in self.x:
                self.x.append(i)
                for y in other.v:
                    if y not in self.x:
                        self.x.append(y)
        return OrderSet(self.x)
    def __sub__(self,other):
        self.x=[]
        for i in self.v:
            if i not in other.v:
                self.x.append(i)
        return OrderSet(self.x)   
        # return OrderSet(
        #     (x for x in self.v if x not in other.v)
        # )
    def __xor__(self,other):
        return (self-other)|(other-self)





s1=OrderSet([1,2,3,4])

s2=OrderSet([3,4,5])

print(s1&s2)
print(s1|s2)
print(s1-s2)
print(s1^s2)