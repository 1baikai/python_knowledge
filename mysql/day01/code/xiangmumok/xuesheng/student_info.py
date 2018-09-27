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
        a=l.index(v)

    n=input("重新输入名字：") 
    L[a]['name']=n 
    

    age=input("重新输入年龄:")
    L[a]['age']=age
    
    c=input("重新输入成绩:")
    L[a]['score']=c

############################################
def cj(L):
    return L["score"]
########################################
def nj(L):
    return L["age"]
##########################################