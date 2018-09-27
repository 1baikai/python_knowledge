# class Human:
#     def set_info(self,name,age,address='不详'):
#         '此方法用来给人对象添加姓名，年龄．家庭住址属性'
#         print(name,age,address)
#         self.name1=name
#         self.age2=age
#         self.address3=address


#     def show_info(self):
#         '此处显示此人的信息'
#         print("姓名:",self.name1,"年纪:",self.age2,"住址：",self.address3)




# h1=Human()
# h1.set_info('校长',20,'天安门')
# h2=Human()
# h2.set_info('小李',18)
# h1.show_info()
# h2.show_info()


# class Student:
#     def __init__(self,name,age,score=None):
#         self.name=name
#         self.age=age
#         self.score=score
#     def set_score(self,score):
#         self.score=score

#     def show_info(self):
#         print(self.name,"今年",self.age,"考了",self.score,"分")


# L=[]
# L.append(Student('小张',29,100))
# L.append(Student('小李',28,90))
# L.append(Student('小白',20))
# print(L)
# L[2].set_score(101)
# for obj in L:
#     obj.show_info()


# class Human:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#         self.money=0
#         self.skill=[]
#     def teach(self,other,skill):
#         print(self.name,'教',other.name,'学',skill)
#         other.skill.append(skill) #让ｏｔｈｅｒ增加技能
#     def work(self,m):
#         print(self.name,'上班赚了',m,'元')
#         self.money+=m
#     def borrow(self,other,m):
#         if other.money>m:
#             print(self.name,'向',other.name,'借',m,'元')
#             other.money-=m
#             self.money+=m
#         else:
#             print(other.name,'没有借钱给',self.name)
#     def show_info(self):
#         print(self.age,'岁的',self.name,'有钱',self.money,'元，它学会的技能：','，'.join(self.skill))

# zhang3=Human("张三",35)
# li4=Human("李四",8)
# wangmazi=Human('王麻子',99)
# zhang3.teach(li4,'python')
# li4.teach(zhang3,'王者容药')
# zhang3.work(1000)
# li4.borrow(zhang3,200)
# li4.show_info()
# wangmazi.teach(zhang3,'lol')
# wangmazi.show_info()
# zhang3.show_info()

# class Human:
#     __slots__=['name','age']
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def info(self):
#         print(self.name,'今年',self.age,'岁')

# h1=Human('小张',8)
# h1.info()
# h1.Age=9
# h1.info()

# class people:
#     country="china"

#     @classmethod
#     def getCountry(cls,):
#         return cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country=country


# p=people()
# print(p.getCountry())
# print(people.getCountry())

# p.setCountry("asd")
# print(p.getCountry())
# print(people.getCountry())

# class Student:
#     count=0
#     def __init__(self,x,y,z):
#         self.name=x
#         self.age=y
#         self.score=z
#         self.__class__.count+=1

#     def dell(self):
#         del self.name
#         del self.age
#         del self.score
#         print(self.name,'被删除')
#         self.__class__.count-=1
#     # def get(self,x,y,z):
#     #     l.append(Student(x,y,z))
#     #     self.__class__.count+=1
#     def pingc(self):
#         return self.score 
#     def pingn(self):
#         return self.age 
# l=[]
# while True:
#     x=str(input("请输入姓名："))
#     if x =="":
#         print("当前人数是：",Student.count)
#         break
#     try:
#         y=int(input("请输入年龄："))
#         if y>=100 or y<=0:
#             print("超出范围．．")
#             continue
#         z=int(input("请输入成绩："))
#         if z>=100 or z<=0:
#             print("超出范围．．")
#             continue

#     except:
#         print("您输入有误．重新输入．．．．")
#         continue
#     l.append(Student(x,y,z))
# sum1=0
# for i in l:
#     i.pingc()
#     sum1=sum1+i.pingc()
# print("平均成绩",sum1/Student.count)


class Human:
    def __init__(self,x):
        self.name=x


    def say(self,name,what):
        print("说",what)

    def walk(self,distance):
        print("走了",distance,"公里")


class Student(Human):
    def study(self,subject):
        print("正在学",subject)

class  Teacher(Human):
    def  teach(self,subject):
        print("z正在教",subject)

# h1=Human()
# h1.say('今天天气真好')
# h1.walk(5)

h2=Student()
h2.say("hello")
h2.walk(9)
h2.study("sguxue")