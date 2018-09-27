# class Mylist(list):
#     def insert_head(self,x):
#         self[0:0]=[x]
#         self.insert(0,x)
# myl=Mylist(range(3,6))
# print(myl)
# myl.insert_head(2)
# print(myl)


# class Human:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a

#     def infos(self):
#         print("name",self.name)
#         print("age",self.age)


# class  Student(Human):
#     pass

# s1=Student('write',200)
# s1.infos()

# class Price(object):
#     a=0
#     def __init__(self):
#         self.price=100
#         self.couunt=0.7
#     def  price(self):
#         new_price=self.price*self.couunt
#         return new_price
# p=Price()
# print(p.price)
# print(p.a)

class Student:
    l=[]
    def __init__(self,n,a,s=0):
        self.name=n
        self.age=a 
        self.score=s 
    @classmethod
    def add(cls):
        while True:
            a=input("姓名：")
            if a=='':
                break
            b=int(input("age:"))
            c=int(input("score"))
            cls.l.append(Student(a,b,c))
            # for i in cls.l:
            #     print(i)

    # @classmethod
    # def dell(cls):
    #     x=input("输入要删除的学生：")
    #     for i in cls.l:
    #         if x in i:
    #             del i
    #         else:
    #             continue

    # @classmethod
    # def paixugao(cls):
    #     cls.l.sorted(cls.l,key=self.score,reversed=True)
    # @classmethod
    # def paixudi(cls):
    #     cls.l.sorted(cls.l,key=self.score,reversed=False)
    # @classmethod
    # def show(cls):
    #     print(self.name,self.age,self.score)

Student.add()
# Student.dell()
# Student.show()

for x in Student.l:
    print(x.name,x.age,x.score)