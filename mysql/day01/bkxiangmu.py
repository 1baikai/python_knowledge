#学生信息管理项目

# L=[]
# while True:
#     d={}
#     x=str(input("请输入姓名："))
#     if x =="":
#         break
#     y=int(input("请输入年龄："))
#     z=int(input("请输入成绩："))
#     d['name']=x
#     d['age']=y
#     d['score']=z
#     L.append(d)
# print(L)
# p=len(L)
# ####
# a='name'
# b='age'
# c='score'
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
# print('|'+a.center(20)+'|'+b.center(10)+'|'+c.center(10)+'|')
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
# i=0
# # for i in range(0,p):
# while i<p:
#     q=L[i]['name']
#     w=str(L[i]['age'])
#     e=str(L[i]['score'])
#     print('|'+q.center(20)+'|'+
#         w.center(10)+'|'+
#         e.center(10)+'|')
#     i=i+1
# print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')



def input_student():
    L=[]
    while True:
        d={}
        x=str(input("请输入姓名："))
        if x =="":
            break
        y=int(input("请输入年龄："))
        z=int(input("请输入成绩："))
        d['name']=x
        d['age']=y
        d['score']=z
        L.append(d)
    return L
###########################################
def get_chinese_char_count(x):
    u=0
    for i in x:
        if 65<=ord(i)<=122:
            continue
        u=u+1
    return u
#################################
def output_student(L):
    p=len(L)
    ####
    a='name'
    b='age'
    c='score'
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+a.center(20)+'|'+b.center(10)+'|'+c.center(10)+'|')
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    i=0

  
    while i<p:
        q=L[i]['name']
        w=str(L[i]['age'])
        e=str(L[i]['score'])
        t = get_chinese_char_count(q)
        print('|'+q.center(20-t)+'|'+
            w.center(10-t)+'|'+
            e.center(10-t)+'|')
        i=i+1
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')

#################################################
def delete_student(L):
    y=input("输入要删除的学生信息：")
    p=len(L)
    l=[]
    i=0
    while i<p:
        Q=L[i]['name']
        if Q not in l :
            l.append(Q)
        i=i+1
   
    if y in l:
        a=l.index(y)
        
        o=L.pop(a)
  
    return o


############################################
def correct_student(L):
    v=input("输入要修改的学生信息：")
    p=len(L)
    l=[]
    i=0
    while i<p-1: 
        Q=L[i]['name']
        if Q not in l :
            l.append(Q)
        i=i+1
    if v in l:
        k=l.index(v)

    n=input("重新输入名字：") 
    L[k]['name']=n 
    

    age=input("重新输入年龄:")
    L[k]['age']=age
    
    c=input("重新输入成绩:")
    L[k]['score']=c

############################################
def cj(L):
    return L["score"]
########################################
def nj(L):
    return L["age"]
##########################################
def main():
    a="1"
    b="2"
    c='3'
    d="4"
    f="5"
    g="6"
    h="7"
    k="8"
    e='q'
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+' '*5+a+')'+'添加学生信息'+' '*23+'|')
    print('|'+' '*5+b+')'+'显示学生信息'+' '*23+'|')
    print('|'+' '*5+c+')'+'删除学生信息'+' '*23+'|')
    print('|'+' '*5+d+')'+'修改学生信息'+' '*23+'|')
    print('|'+' '*5+f+')'+'按学生成绩高－低显示系学生信息'+' '*5+'|')
    print('|'+' '*5+g+')'+'按学生成绩低－高显示系学生信息'+' '*5+'|')
    print('|'+' '*5+h+')'+'按学生年龄高－低显示系学生信息'+' '*5+'|')
    print('|'+' '*5+k+')'+'按学生年龄低－高显示系学生信息'+' '*5+'|')
    print('|'+' '*5+e+')'+'退出'+' '*31+'|')
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    L=[]
    while True:
        x=input("请选择：")

        if x is a:
            L += input_student()
            print(L)
        elif x is b:
            output_student(L)
        elif x is c:
            delete_student(L)
        elif x is d:
            correct_student(L)
        elif x is f:
            L=sorted(L,key=cj,reverse=True)
            output_student(L)
        elif x is g:
            L=sorted(L,key=cj,reverse=False)
            output_student(L)
        elif x is h:
            L=sorted(L,key=nj,reverse=True)
            output_student(L)
        elif x is k:
            L=sorted(L,key=nj,reverse=False)
            output_student(L)

        else:
            x is e
            break
main()