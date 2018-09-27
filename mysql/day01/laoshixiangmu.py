# L=[]  #创建一个新的列表，用此列表保存学生信息
# #录入学生信息：
# while True:
#     n=input("请输入姓名")
#     if not n :
#         break
#     a=int(input("请输入年龄："))
#     s=int(input("请输入成绩："))
#     #创建一个新的字典，把学生的信息存入字典中
#     d={} #每次都重新创建一个新的字典
#     d['name']=n
#     d['age']=a
#     d['score']=s
#     L.append(d)
# print(L)
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
# print('|'+'name'.center(20)+'|'+'age'.center(10)+'|'+'score'.center(10)+'|')
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
# for d in L:
#     n=d['name']
#     a=d['age']
#     s=d['score']
#     print('|%s|%s|%s|'%(n.center(20),
#                    (str(a)).center(10),
#                    (str(s)).center(10)
#                         )
#          )
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')

def input_student():
    L=[]  #创建一个新的列表，用此列表保存学生信息
#录入学生信息：
    while True:
        n=input("请输入姓名")
        if not n :
            break
        a=int(input("请输入年龄："))
        s=int(input("请输入成绩："))
        #创建一个新的字典，把学生的信息存入字典中
        d={} #每次都重新创建一个新的字典
        d['name']=n
        d['age']=a
        d['score']=s
        L.append(d)
    return L
def output_student(L):
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+'name'.center(20)+'|'+'age'.center(10)+'|'+'score'.center(10)+'|')
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    for d in L:
        n=d['name']
        a=d['age']
        s=d['score']
        print('|%s|%s|%s|'%(n.center(20),
                       (str(a)).center(10),
                       (str(s)).center(10)
                            )
             )
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
L=input_student()
print(L)
output_student(L)