class Student:
    
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.score=z
        # print(x,y,z)
    def show_info(self):
        # print(self.name,"今年",self.age,"考了",self.score,"分")
        o=[]
        o.append(self.name)
        
        o.append(self.age)
        
        o.append(self.score)
        print(o)
    # def show_age(self):
    #     r=[]
    #     r.append(self.age)
    #     print(r)

L=[]
while True:
    x=str(input("请输入姓名："))
    if x =="":
        break
    try:
        y=int(input("请输入年龄："))
        if y>=100 or y<=0:
            print("超出范围．．")
            continue
        z=int(input("请输入成绩："))
        if z>=100 or z<=0:
            print("超出范围．．")
            continue

    except:
        print("您输入有误．重新输入．．．．")
        continue
    L.append(Student(x,y,z))
# print(L)

for i in L:
    i.show_info()
    # i.show_age()

# def output_student(L):
#     p=len(L)
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
#     print('|'+'name'.center(20)+'|'+'age'.center(10)+'|'+'score'.center(10)+'|')
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
#     i=0
#     while i<p:
#         q=L[i]['name']
#         w=str(L[i]['age'])
#         e=str(L[i]['score'])
#         t = get_chinese_char_count(q)
#         print('|'+q.center(20-t)+'|'+
#             w.center(10)+'|'+
#             e.center(10)+'|')
#         i=i+1
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
