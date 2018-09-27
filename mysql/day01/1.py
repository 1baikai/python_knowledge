# x=int(input("请输入长度："))
# y=int(input("请输入宽度："))
# print("长方形的周长为",(x+y)*2,"厘米")
# print("长方形的面积为", x*y,"平方厘米")
# pi=3.141592653
# r=float(input("请输入半径："))
# print("圆的周长是",pi*r*2,"CM")
# print("圆的面积是",pi*r**2,"平方CM")



# 第一题
# print("   *")
# print("  ***")
# print(" *****")
# print("*******")



#第二题
# print("中国古代的２１６两是",216//16,"斤",216%16,"两")



#第三题
# x=int(input("请输入秒数："))
# a=x//(60*60)
# b=(x%3600)//60
# c=x%3600%60
# print(a,"时",b,"分",c,"秒")


#第四题
# huashi=float(input('请输入：'))
# sheshi=5.0/9.0*(huashi-32)
# kaishi=sheshi+273.15
# print(huashi,"华氏温度转换为摄氏温度是",sheshi,"度")
# print("开氏温度是",kaishi)

# a=int(input("请输入小时："))
# b=int(input("请输入分："))
# c=int(input("请输入秒："))
# print("距离",a,":",b,":",c,"过了",a*60*60+b*60+c,"秒")


# x=int(input("输入ｘ："))
# y=int(input("输入y："))
# a=x+y
# b=x*y
# c=pow(x,y)
# print(x,"+",y,"=",a)
# print(x,"*",y,"=",b)
# print(x,"**",y,"=",c)



# x=int(input("请输入一个整数："))
# if x<0:
#     print(x,"小于0")
# elif 0<x<80:
#     print(x,"在80～100之间　")
# else:
#     x>100
#     print(x,"大于100")



# x=int(input("请输入任意一个季度："))

# if x==1:
#     print("这个季度有１２３月")
# elif x==2:
#     print("这个季度有4 5 6 月")
# elif x==3:
#     print("这个季度有7 8 9 月")
# elif x==4:
#     print("这个季度有10 11 12 月")
# else:
#     print("你输错啦傻逼")

# x=int(input("请输入任意一个月份："))
# if x in range(1,4):
#     print("这个月在第一季度")
# elif x in range(4,7):
#     print("这个月在第二季度")
# elif x in range(7,10):
#     print("这个月在第三季度")
# elif x in range(10,13):
#     print("这个月在第四季度")
# else:
#     print("您输错啦")


# x=int(input("请输入一个数："))
# if x>0:
#     print(x)
# else:
#     print(-x)

# x=int(input("请输入一个数："))
# a=x if x>0 else -x
# print(a)


# score=int(input("请输入学生成绩："))
# if 0 <=score<=100:
#     pass
# else:
#     print("输入不合法!")


# print("你是不是傻？")
# a=str(input("请输入yes或no:"))
# if a=='yes':
#     print("你就是傻！")
# else:
#     print("shabi")


# x=float(input("请输入公里数："))
# if x<=3:
#     print("走了",x,"公里","花了",13,"元")
# elif 3<=x<=15:
#     print("走了",x,"公里","花了",round(2.3*(x-3)+13),"元")
# else:
#     print("走了",x,"公里","花了",round(3.45*(x-15)+12*2.3+13),"元")


# a=float(input("shurukemuyi:"))
# b=float(input("shurukemuer:"))
# c=float(input("shurukemusan:"))
# if a>b :
#     max=a
#     if max>c:
#         max=a
#     else:
#         max=c
# else:
#     max=b
#     if max>c:
#         max=b
#     else:
#         max=c
# print("zuidadeshi",max)
# if a>b :
#     min=b
#     if min>c:
#         min=c
#     else:
#         min=b
# else:
#     min=a
#     if min>c:
#         min=c
#     else:
#         min=a
# print("zuixiaozhi",min)
# print("pingjunzhi",(a+b+c)/3)

# 方法２：
# zuida=a
# if b >zuida :
#     zuida =b
# if c>zuida :
#     zuida =c
# print("最大是",zuida)


# x=int(input("请输入年份："))
# if x % 100!=0 and x%4==0:
#     print("shi")
# elif x%400==0:
#     print ("shi")
# else:
#     print("bushi")


# t=float(input("请输入体重："))
# s=float(input("请输入身高："))
# bmi=t/s**2
# print("bml是:",bmi)
# if bmi<18.5:
#     print("多吃点吧")
# elif 18.5<bmi<=24:
#     print("保持吧")
# else:
#     print("该减肥了")



# X=str(input("请输入一段话："))
# a="白凯"
# if a in X:
#     print("您的名字出现了")
# else:
#     print("没出现")

# a=str(input("请输入："))
# print(a[0])
# print(a[-1])
# if len(a)%2==1:
#     print(a[len(a)//2])
# else:
#     pass


# x=str(input("请输入："))
# print(x[1:len(x)-1])


# a=str(input("请输入："))
# if a[:]==a[::-1]:
#     print("shihuiwen")
# else:
#     print("bushi ")


# a=str(input("请输入："))
# if " " in a:
#     print("有",a.count(" "),"空格")

#     print("去掉空格后为",a.strip())
# b=a.isdigit()
# if b<100:
#     print(b,"budayu100")
# else:
#     print(b,"dayu100")
  

# a=int(input("请输入数字："))

# print(a*" ","   *",sep='')    
# print(a*" ","  ***",sep='') 
# print(a*" "," *****",sep='')  
# print(a*" ","*******",sep='')     

# # a=str(input("请输入："))
# # b=a.replace(" ",'')
# # print(b,len(b))

# a=str(input("请输入："))
# b=str(input("请输入："))
# c=str(input("请输入："))
# max=len(a)
# if len(b) >max:
#      max =len(b)
# if len(c)>max:
#      max =len(c)
# v=a.center(max+5)
# j=b.center(max+5)
# p=c.center(max+5)
# print("+",(max+5)*'-',"+")
# print("|",v,"|")
# print("|",j,"|")
# print("|",p,"|")
# print("+",(max+5)*'-',"+")


# a=str(input("请输入１："))
# b=str(input("请输入2："))
# c=str(input("请输入3："))
# i=max(len(a),len(b),len(c))
# print(" "*(i-len(a)) +a)
# print(" "*(i-len(b)) +b)
# print(" "*(i-len(c)) +c)


# i=1     #  i变量用于控制循环条件
# while i <=20:    #如果条件为TRUE
#     print("hello")
#     i+=1      #改变循环条件以便让循环终止
# else:
#     print("这时else子句，此时将离开while语句")
#     print("此时i的值是：",i)  # 4


# i=0
# while i <20:
#     i+=1
#     print(i)
# # 


# i=0

# while i<20:

#     i+=1
#     print(i,end=" ")
#     if i%5==0:
#         print()

#       
# i=0.0
# while i<10.0:
#     print(i)  
#     i+=0.5


# i=0
# a=0
# while i<=100:
#     sum=sum+i
#     i+=1
# print(sum)

# begin=int(input("请输入一个开始数："))
# end=int(input("请输入一个结束数："))
# i=0
# while begin<=end:
#     i=i+1
#     if i%5!=0:
#         print(begin,end=" ")       
#     else:
#         print(begin)
#     begin=begin+1
#



# i=1
# n=int(input("请输入正方形边长："))
# while i<=n:
#     a=1
#     while a<=n:   
#         print(a,end=" ")
#         a=a+1
#     print()
#     i=i+1


# i=0
# while True:
#     x=int(input("请输入整数：")) 

#     if x<0:
#         break
#     i=i+x 
# print("你刚才输入的这些数和是：",i)



# n=int(input("yige zhengshu :"))

# print("#"*n)
# i=1
# while i<=(n-2):
#     # print("#",(n-2)*" ","#",sep="")
#     print("#"+(n-2)*" "+"#")
#     i=i+1
# if n!=1:
#     print("#"*n)


# n=int(input("请输入ｎ＝"))
# s=0
# a=0
# while a<=n:    
#     i=1/(2**a)
#     a=a+1
#     s=s+i
# print(s)





# n=int(input("请输入ｎ＝"))
# a=0
# b=0
# s=0
# while b<n:
#     b=b+1
#     x=(-1)**a/(2*b-1)
#     a=a+1
#     s=s+x
# y=s*4
# print(s)
# print(y)
  




# n=int(input("请输入ｎ"))

# l=1
# while l<=n:
#     print("*"*l)
   
#     l=l+1
# l=1
# while l<=n:
#     print(" "*(n-l)+"*"*l)
#     l=l+1
    
# l=0
# while l<n:
#     print(" "*l+"*"*(n-l))
#     l=l+1
# l=0   
# while l<n:
#     print("*"*(n-l)+" "*l)
#     l=l+1

# i=1
# while i:
#     j=1
#     while j:
#         print(j,"*",i,"=",i*j, end="  ")
#         if i ==j :
#             break
#         j=j+1
#         if j>=10:
#             break
#     print()
#     i=i+1
#     if i>=10:
#         break

#生成10行
# j = 0
# while j < 10:
#     # 生成1行10列的星星
#     i = 0
#     while i < 10:
#         #判断奇数行还是偶数行
#         if j % 2 == 0:#偶数行
#             print('★', end=' ')
#         else:#奇数行
#             print('☆', end=' ')
#         i += 1
#     # 输出换行符号
#     print('\n', end='')
#     #j自增
#     j += 1

# x=str(input("请输入名字："))
# y=str(input("请输入年龄："))
# print("%s今年%s岁" %x,%y)

# str1="         MＹ name is mr green    "
# str2="hello"
# print(str1.strip())

#for.py
# s="ABCD"
# for ch in s:
#     print("ch--->>",ch)
# 答案：
# # ch--->> A
# # ch--->> B
# # ch--->> C
# # ch--->> D

#练习：１＼任意输入一段字符串，
#1计算出输入字符＂a＂的个数，并打印出个数
#计算出空格的二个书，并打印出个数
# s=str(input("请输入："))
# x=0
# y="a"
# for y in s :
#     if y == 'a':
#         x=x+1
# print(x)
# z=" "
# i=0
# for  z in s:
#     if z ==" ":
#         i=i+1
# print(i)

# s=input("qingshuru")
# count_a=0
# for c in s:
#     if c =="a":
#         count_a=count_a+1
# else:
#     print("adegeshu:",count_a)

# count_blank=0
# for c in s :
#     if c ==" ":
#         count_blank=count_blank+1
# print("kongge",count_blank)


#for_else.py
# s=input("请输入：")
# for ch in s :
#     if ch == "H":
#         print(s,"zhonghanyou zifu 'h'")
#         break
# else:
#     print(s,"buhanyou 'H'")
#


#while
# s=input("请输入：")
# i=0
# while i<len(s):
#     ch=s[i]
#     if ch =="H":
#         print(s,"zhonghanyou zifu 'h'")
#         break
#     i=i+1
# else:
#     print(s,"buhanyou 'H'")


#range.py
# for x in range(4):
#     print(x)  #0,1,2,3
# else:
#     print("可迭代对象已经不能提供数据了")


# for x in range(1,21):
#     print(x,end=" ")

#while
# n=1
# s=0
# while 1:
    
#     a=2*n-1
#     s=s+a
#     n=n+1
#     if a>=99:
#         break
# print(s)

#for
# s=0
# for x in range(1,100,2):
#     s=s+x
# print(s)

# for x in "ABC":
#     for y in "123":
#         print(x+y)

# 
# for x in range(1,101):
#     if x*(x+1)%11==8:
#         print(x)

# n=int(input("请输入n"))
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print(y,end=" ")
#     print()

# n=int(input("请输入n"))
# for x in range(1,n+1):    
#     for y in range(x,x+n+1):                
#         print("%2d"%y,end=" ")
#     print()

# for x in range(65,91):
#     print(str(chr(x)),end=" ")
# print()
# for y in range(65,91):
#     print(str(chr(y)+chr(y+32)),end=" ")
# print()
#************
# s=""
# for code in range (ord("a"),ord("z")+1):
#     s+=chr(code)
# print(s)
# s2=""
# for code in range(65,65+26):
#     s2+=chr(code)
#     s2+=chr(code+32)
# print(s2)  
#********全世界的字*********
# for code in range (0,65536):
#     ch=chr(code)
#     print(ch,end="")
#**********************

# for x in range(1,101):
#     if x%7==0 or x%10==7 or x//10==7:
#         print(x)
#     else:
#         continue

# a=str(input("请输入："))
# b=str(input("请输入："))
# c=str(input("请输入："))
# L=[a,b,c]
# print(L)
# a=0
# L=[]
# while True:
#     x=str(input("请输入"))
#     if x == "":
#         break
#     L=L+[x]
#     a=a+1
# print(L)
# print(a)

#####素数####
# x=int(input("请输入一个数："))
# i=1
# while i<x-1:
#     i=i+1
#     if x%i==0:
#         print("bushi")
#         break
#     else:
#         continue
# else:
#     print("shi")
#***********************************
#laoshinb
# x=int(input("请输入一个数："))
# if x<2:
#     print(x,"不是素数")
# else:
#     for i in range(2,x):
#         if x%i==0:
#             print(x,"不是素数")
#             break
#         else:
#             print(x,"是素数")

#**********************************
# x=int(input("请输入一个数："))
# for a in range(2,x-1):
#     if x%a==0:
        
#         print("no")
#         break
# else:
#     print("yes")

#         
#         
#***********************************


# x=int(input("请输入整数："))
# d=len("*"*(2*x-1))
# for a in range(1,x+1):
#     b="*"*(2*a-1)
#     c=b.center(d)
#     print(c)
# for a in range(1,x+1):
#     t=str("*")
#     z=t.center(d)
#     print(z)


# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             x=a*100+b*10+c
#             if x ==a**3+b**3+c**3:
#                 print(x)

# for a in range(100,1000):
#     x=a//100
#     y=(a%100)//10
#     z=a%100%10
#     if x*100+y*10+z==x**3+y**3+z**3:
#         print(a)

# for a in range(100,1000):
#     s=str(a)
#     x=int(s[0])
#     y=int(s[1])
#     z=int(s[2])
#     if a==x**3+y**3+z**3:
#         print(a)

# a=0
# l=[]
# while True:
#     x=int(input("请输入整数："))
    
    
#     if x==-1:
        
#         break
#     l[len(l):]=[x]
#     a=a+1
# print(l)
# print("您共输入了%d个有效数字"%a)
# print(max(l))
# print(min(l))
# print(sum(l)/a)

# #     
# a=0
# l=[]
# while True:
#     x=int(input("请输入整数："))
#     if x<=0:
#         break
#     l[len(l):]=[x]
#     a=a+1
# print("第一大：",max(l))
# b=l.index(max(l))
# del l[b]
# print("第二大：",max(l))
# print("最小的：",min(l))
# l.remove(min(l))
# print("最后结果：",l)

# l=[]
# while True:
#     x=int(input("yigeshu:"))
#     if x<0:
#         break
#     l.append(x)

# zuida=max(l)
# print("zuidadeshi",max(l))
# l2=l.copy()
# while True:
#     if zuida in l2:
#         l2.remove(zuida)
#     else:
#         break
# print("dierdadeshushi",max(l2))
# zuixiao =min(l)
# while zuixiao in l:
#     l.remove(min(l))
# print("zuihoudejieguoshi",l)

# l="hello"
# l=' '.join(l)
# print(l)

# l=[2*n-1 for n in range(1,51)]
# print(l)

# l=[i for i in range(1,100) if i%2==1]
# print(l)

# begin=int(input("请输入一个数："))
# end=int(input("请输入一个数："))
# l=[i for i in range(begin,end) if i%2==0]
# print(l)

# begin=int(input("请输入一个数："))
# end=int(input("请输入一个数："))
# l=[]
# for x in range(begin,end):
#     if x%2==0:
#         l.append(x)
# print(l)

# a="ABC"
# b="123"
# l=[x+y
#     for x in a
#         for y in b]
# print(l)

# s='100,200,300,500,800'
# l=s.split(",")
# print(l)
# a=[int(x) for x in l ]
# print(a)

###########################
# l=[]
# while True:
#     y=int(input("请输入："))
#     if y<0:
#         break
#     l.append(y)
# print(l)
# l2=[]
# for a in l:
#     if  a not in l2:
#         l2.append(a)
# print("去掉重复的：",l2)
# l3=[]
# for x in l :
#     i=l.count(x)
#     if i==2:
#         l3.append(x)
# l4=[]
# for s in l3:
#     if s not in l4:
#         l4.append(s)
# print("出现俩次的：",l4)
#*****************************
#day06
# L=[1,3,2,1,6,4,2,98,82]
# L2=[]
# for x in L:
#     if x not in L2:
#         L2.append(x)
# print("L2=",L2 )
# L3 =[]
# for x in L:
#     if x not in L3 and L.count(x)==2:
#         L3.append(x)
# print('L3=',L3)




# l=[]
# for x in range(1,101):
#     if x<2:
#         pass
#     else:
#         for i in range(2,x):
#             if x%i==0:
                
#                 break
#         else:
#              l.append(x)
# print(l,"是素数")
###laoshi nb###
# L=[]
# for x in range(100):
#     if x<2:
#         continue
    
#     for i in range(2,x):
#         if x %i ==0:
#             break
#         else:
#             continue
#     else:
#         L.append(x)
# print(L)


# l=[]
# a=0
# b=1
# while b<1000:
#     l.append(b)  
#     a,b=b,a+b
# print(l)

# l=[1,1]erf ewr
# while len(l)<40:
#     l.append(l[-1]+l[-2])
# print(l)

######LAOSHI##
# L=[]
# a=0
# b=1
# while len(L)<40:
#     L.append(b)  #把已经得道德数加入列表中
#     #在算出下一个数，依旧存于ｂ中，为下次循环做准备
#     c=a+b  #下一次的数
#     a=b#将当前的数交给ａ
#     b=c#再把已经算好的交给ｂ
# print(L)

# d={1:'春季有1,2,3月',
#     2:'夏季有4,5,6月',
#     3:'秋季有7,8,9月',
#     4:'冬季有10,11,12月',}
# x=str(input("请输入一个数："))
# if x in d:
#     print(d[x])
# else:
#     print("没有信息")



# x=str(input("请输入："))
# d={}
# for y in b:
    
#     if y not in d :
#         d[y]=1
#     else:
        
#         d[y]=d[y]+1
# print(d)



# x=str(input("请输入："))

# d={}
# for y in x:
#     i=1
#     if y not in d :
#         d[y]=i
#     else:
#         i=i+1
#         d[y]=i
# print(d)



# d={}
# L=['HAH','XIIX','HEHee']
# a=len(L[0])
# b=len(L[1])
# c=len(L[2])
# d[L[0]]=a
# d[L[1]]=b
# d[L[2]]=c
# print(d)

# L=['HAH','XIIX','HEHee']
# d={x:len(x) for x in L}
# print(d)
#第一题
# d={}
# while True:
#     x=str(input("请输入单词："))
#     if x=="":
#         break
#     y=str(input("请输入解释："))
#     d[x]=y
# print(d)
# y=str(input("请输入单词："))
# if y in d:
#     print(d[y])
# else:
#     print("没有这个单词")



# s={'曹操','刘备','孙权'}
# s1={'曹操','孙权','张飞','关羽'}
# #1
# print(s&s1)
# #2
# print(s-s1)
# #3
# print(s1-s)
# #4
# print( '张飞' in s)
# #5
# print(s^s1)
# #6
# print(len(s|s1))
##########################
# def say_hello():
#     print("hello world")
#     print("i love u")
#     print("hello everyone")
# say_hello()
# print(say_hello())
# say_hello()
##############################

# def mymax(a,b):
#     if  a> b :
#         print("最大是",a)
#     else :
#         print("最小是",b)

# mymax(100,200)
# mymax(50,30)
# mymax("abc","123")


# x=int(input("请输入第一个数："))
# y=int(input("请输入第二个数："))
# def myadd(x,y):
#     print("您输入的俩个数的和是：",x+y)
# myadd(x,y)


# def myadd(a,b):
#     s=a+b
#     return s
# a=int(input("请输入第一个数："))
# b=int(input("请输入第二个数："))
# print("您输入的俩个数的和是：",myadd(a,b))

# def mymax(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(mymax(100,200))
# print(mymax("ABCD","ABC"))

# def input_number():
#     L=[]
#     while True :
#         x=int(input("请输入"))
#         if x <0:
#             break
#         L.append(str(x))
#     return L
# L=input_number()

# print(L)
# print("最大值",max(L))
# print("最XIAO值",min(L))
# print("HE",sum (L))


####有问题＃＃＃＃＃＃
# def input_number():
#     L=[]
#     while True :
#         x=int(input("请输入"))
#         if x <0:
#             break
#         L.append(str(x))
#     print(L)
# v=input_number()
# # input_number()
# print (max(v))
##########################

# def fun(n):
#     Sn =0
#     for a in range(1,n+1):
#         Sn =Sn +1/a
#     return Sn
# print(fun(3))
# print(fun(12))

# def fun2(n):
#     s=0
#     for x in range (1,n+1):
#         s+= 1 / ( x * ( x + 1 ))
#     return s
# print(fun2(3))
# print(fun2(1000))




# def myfn(n):
#     import time
#     i=0
#     while True:
#         print("hello")
#         if i==n:
#             break
#         i=i+1
#         time.sleep(1)
# myfn(5)


# def get_chinese_char_count(x):
#     a=0
#     for i in x:
#         if 65<=ord(i)<=122:
#             continue
#         a=a+1
#     return a
# x=input("输入中英文混合的字符串：")
# print("您输入中文的字符个数是：",get_chinese_char_count(x))


# def isprime(x):
    
#     if x==2:
#         return True
#     for i in range(2,x):
#         if x%i==0:
#             return False
#             break
#     else:
#         return True
# print(isprime(27))
# print(isprime(16))


# def prime_m2n(m,n):
#     l=[]
#     for x in range(m,n):
#         if x ==2:
#             l.append(x)
#         i=1
#         while i <x-1:
#             i=i+1
#             if x%i ==0:
#                 break
#             else:
#                 continue
#         else:
#             l.append(x)
#     return l
# l=prime_m2n(3,15)
# print(l)

# def primes(n):
#     l=[]
#     for i in range(1,n):
#         if i <2:
#             continue
        
#         for a in range(2,i):#取到６时取不了了，所以执行else
#             if i % a==0:
#                 break
#             else:
#                 continue  
#         else:
#             l.append(i)
#     return l
# l=primes(100)
# print(l)
# print(sum(l))
# l=primes(200)
# print(sum(l))

# 1位置传参
# def myfun(a,b,c):
#     print('a的值是：',a)
#     print('b的值是：',b)
#     print('c的值是：',c)

# myfun(1,2,3)
# myfun(4,5,6)
# ２序列传参
# def myfun(a,b,c):
#     print('a的值是：',a)
#     print('b的值是：',b)
#     print('c的值是：',c)
# s1=[11,22,33]
# s2=(44,55,66)
# s3="ABC"
# myfun(*s1)#myfun(s1[0],s1[1],s1[2])
# myfun(*s2)#myfun(s2[0],s2[1],s2[2])
# myfun(*s3)#myfun(s3[0],s3[2],s3[2])
# 3 按关键字传参
# def myfun(a,b,c):
#     print('a的值是：',a)
#     print('b的值是：',b)
#     print('c的值是：',c)
# myfun(c=33,b=22,a=11)
# myfun(b=330,c=220,a=110)
# 4 字典传参
# def myfun(a,b,c):
#     print('a的值是：',a)
#     print('b的值是：',b)
#     print('c的值是：',c)
# d1={"c":300,"b":200,"a"=:100}
# myfun(**d1)#myfun(a=d1['a'],b=d1['b'],c=d1['c'])

# def getminmax(a,b,c):
#     t=(min(a,b,c),max(a,b,c))
#     return t
# print(getminmax(2,4,67))

#5
# def info(name,age=1,address='不详'):
#     print('我叫',name,'我今年',age,'岁，我的住址',address)
# info('菜鸡',23,'军事基地')

# def myadd(a=0, b=0, c=0, d=0):
#     # print('sum=',a+b+c+d)
#     x=a+b+c+d
#     return x
# print(myadd(100,200))
# print(myadd(100,200,300))
# print(myadd(100,200,300,400))

def myrange(start,stop=None,step=1):
    if stop is None:
        stop =start
        start=0
    l=[]
    i=start
    if step >0:
        while i<stop:
            l.append(i)
            i+=step
        return(l)
    elif step<0:
        while  i <stop:
            l.append(i)
            i+=step
        return l
l=myrange(5)
l=myrange(5,10,-2)
print(l)

# def fun(*arfs):
#     print("实参的个数是",len(args))
#     print('args=',args)
#     
#diyizhong
# def mysum(*args):
#     a=sum((args))
#     return a
# print(mysum(1,2,3,4))
#dierzhong
# def mysun(*args):
#     s=0
#     for x in args:
#         s=s+x
#     return s
# print(mysun(1,2,3,4,5))
#################################
# def mymax(a,*args):
#     i=1
#     zuida =args[0]
#     for x in args:
#         if x>zuida:
           
#             zuida=x

#             continue
#         else:
#             args[i]<args[i]
###################################33
# def mymax(a,*args):
#     if not args:
#         zuida =a[0]
#         for x in a :
#             if x>zuida :
#                 zuida =x
#         return zuida 
#     else:
#         zuida=a
#         for x in args:
#             if x>zuida :
#                 zuida =x
#         return zuida 
# print()

#7此实例命名关键字传参
# def fun(*,c,d):
#     print('c=',d)
#     print('d=',d)
# fun(3,4) #chucuo
# fun(d=4,c=3)


# def fun2(a,b,*,c,d):
# fun2(1,2,c=3,d=5)

# def fun3(a,b,*args,c,d):
#     print(a,b,args,c,d)
# fun3(11,22,33,44,55,c=66,d=77)

# def fun(**kwargs):
#     print("关键字传参的个数",len (kwargs))
#     print("kwargs",kwargs)
# fun(name='baikai',age=10,address='G港')

# def mysum(n):
#     i=1
#     s=0
#     while i<=n:
#         s=s+i
#         i=i+1
#     return s
# print(mysum(100))


#1实例全局局部
# a=100#全局
# b=200#全局
# def fx(c):#d是局部
#     d=400#d是局部
#     print(a,b,c,d)
# fx(300)

# L=[]
# def input_number():
#     L2=[]
#     while True:
#         n=int(input("请输入正整数"))
#         if n< 0:
#             break
#         L2.append(n)
#     #L=L2#创建局部变量，未改变全局变量Ｌ的绑定关系
#     #L.extend(L2)#根据变量找到列表，改变的是列表而不是变量
#     #L+=L2
#     return L2
# L=input_number()
# print(L)


# a=1
# b=2
# c=3
# def fn(c,d):
#     e=300
#     print("locals()返回",locals())
#     print("globals()返回",globals()ian)

# fn(100,200)

#函数名fn是变量，他绑定一个函数对象
# def fn():
#     print("hello world")

# f1=fn
# print(f1)
# print(fn)
# print(f1())  #  none

# def f1():
#     print("函数f1被调用")
# def f2():
#     print("函数f2被调用")
# f1,f2=f2,f1
# f1()
# f2()
#
#此实例一个函数可以做别一个函数的实参传入一个函数中
# def f1():
#     print("hello f1")
# def f2():
#     print("hello f2")
# def fx(fn):
#     print(fn)
#     fn()
# fx(f1)
# fx(f2)

# def goodbye(L):
#     for x in L :
#         print("再见",x)
# def hello(L):
#     for x in L :
#         print("你好",x)
# def do_things(L):
#     fn(L)
# do_things(hello,['a','g','r'])

# def get_function():
#     s=input("请输入您要做的操作")
#     if s=='求最大':
#         return max 
#     elif s=='求最小':
#         return min
#     elif s=="q求和":
#         return sum
# l=[1,2,3,45,6,7]
# f=get_function()
# print(f(l))

# def myadd(x,y):
#     return x+y
# def mysub(x,y):
#     return x-y
# def mymul(x,y):
#     return x*y


# def get_function(op):

#     if op =='+' or '加':
#         return myadd
#     elif op=='-' or '减' :
#         return mysub
#     elif op=='*' or '乘':
#         return mymul


# #在住函数中程序如下：
# def main():
#     while True:
#         s=input("输入计算公式")
#         L=s.split()
#         a=int(L[0])
#         b=int(L[2])
#         fn=get_function(L[1])
#         print("结果是",fn(a,b))
# main()


# def fn_outter():
#     print('fn_outter()被调用')
#     def fn_inner():
#         print("fn_inner被调用")
#     fn_inner()
#     fn_outter()
#     print('fn_outter()结束调用')
# fn_outter()


# def myadd(x,y):
#     return x + y

# myadd=lambda x,y :x+y
# print ('20+30=',myadd(20,30))
# print ('40+50=',myadd(40,50))

# fx=lambda n:(n**2+1)%5==0
# print(fx(3))
# print(fx(4))

# def mymax(x,y):
#     if x>y:
#         return x
#     else:
#         return y


# mymax=lambda x,y:max(x,y)
# print(mymax(100,200))
# mymax=lambda x,y:x if x>y else y

# def myfac(n):
#     s=1
#     for i in range(1,n+1):
#         s=s*i
#     return s
# print(myfac(5))

# def myfac(n):
#     s=0
#     for i in range(1,n+1):
#         s=s+i**i
        
#     return s
# print(myfac(5))

#
# def f(n):
#     return sum(map(lambda  x:x**x,range(1,n+1)))
# print(f(3))

# def sanjiao(n):
    
#     l=[[1],[1,1]]
#     for i in range(2,n):
#         a=l[i-1]
#         b=[1]
#         for j in range(i-1):
#             b.append(a[j]+a[j+1])
#         b.append(1)
#         l.append(b)
#     return l
# print(sanjiao(6))

# def sanjiao(n):
#     q=[]
#     for a in range(n):
#         for b in range(len(q)-1):
#             q.append(q.pop(0)+q[0])
#         q.append(1)
#         print(q)
# sanjiao(6)



####laoshisanjiao #
# def get_next_line(L):
#     #此函数将用一层的了表Ｌ计算下一层，然后返回
#     #l=[1,3,3,1],则返回：［1，4，6，4，1］
#     line=[1]
#     for i in range(len(L)-1):
#         line.append(L[i]+L[i+1])

#     line.append(1)
#     return line

# def get_yh_list(n):
#     L=[]
#     line=[1]
#     for _ in range(n):
#         L.append(line)
#         line=get_next_line(line)
#     return L
# L=get_yh_list(6)
# print(L)

# def list_to_string(L):
    #此函数任意给定一个列表，将其转换为字符串如：Ｌ＝［１，３，３，１］返回＇＇



# def power2(x):
#     return x**2
# l=[]
# for x in map(power2,range(1,10)):
#     l+=[x]
# print(sum(l))

# def power3(x):
#     return x**3
# l=[]
# for x in map(power3,range(1,10)):
#     l+=[x]
# print(sum(l))

# 方法２：
# s=0
# for x in map(lambda x:x**2,range(1,10)):
#     s+=x
# print(s)
# 3
# print(sum(map(lambda x :x**2,range(1,10))))


# def mypow(x,y):
#     return x**y
# for i in map(mypow,range(1,5),range(4,0,-1)):
#     print(i)

# for i in map(pow,[1,2,3,4],[4,3,2,1]):
#     print(i)

# for i in map(pow,[1,2,3,4],[4,3,2,1],range(5,1000)):
#     print(i)

# print(sum(map(pow,range(1,10),range(9,0,-1))))

# def isodd(x):
#     return x%2==1
# for x in filter(isodd,range(10)):
#     print(x)
# print(isodd(5))
# L=list(filter((lambda X:X%2==0),range(1,21)))
# print(L)


# def isprime(x):
    
#     if x==2:
#         return True
#     for i in range(2,x):
#         if x%i==0:
#             return False
#             break
#     else:
#         return True
# L=list(filter(isprime,range(2,101)))
# print(L)


# names=['Tom','Jerry','Spike','Tyke']
# def k(s):
#     return s[::-1]

# names=sorted(names,key=k)
# print(names)

# def f():
#     print("从前有座山，山上有座庙，庙里有个老和尚")
#     f()
# print("开始将故事")
# f()
# print("递归完成")
# def fex(n):
#     print("递归进入第",n,"层")

#     print("递归退出第",n,"层")
# fx(1)
# print("程序结束")


#用递归实现求和：
# def mysum(n):
#     if n==1:
#         return 1
#     return n+mysum(n-1)

# print(mysum(100))  

# def make_power(y):
#     def fn(x):
#         return x **y 
#     return fn
# pow2=make_power(2)
# print("5的平方是：",pow2(5))


# def fx(a,b,c):
#     def fn(x):
#         return a*x**2+b*x+c
#     return fn
# f1= fx(1,2,3)
# print(f1(20))

# def sui(x):
#     if x ==1:
#         return 10
#     return 2+sui(x-1)
# print(sui(5))

# def jc(i):
#     if i==1:
#         return 1
#     return i*jc(i-1)
# def jch(s):
#     l=[]
#     for i in range(1,s+1):
#         jc(i)
#         l.append(jc(i))
#     return l
        
# print(sum(jch(20)))

# def jc(i):
#     if i ==1:
#         return 1
#     return i*jc(i-1)
# def jch(i):
#     if i==1:
#         return 1
#     return jc(i)+jch(i-1)
# print(jch(20))

# def emm(l):
#     for i in l:
#         if type(i) is int :
#             a.append(i)
#         else:
#             emm(i)
#     return a
# a=[]
# L=[[3,5,8],10,[[13,14],15,18],20]
# # print(emm(L))
# def print_list(lst):
#     for x in lst:
#         if type(x) is list :
#             print_list(x)
#         else:
#             print(x)

# print_list(L)
# def sum_list(lst):
#     s=0
#     for x in lst:
#         if type(x) is int:
#             s+=x
#         elif type(x) is list:
#             print(x)
#             s+=sum_list(x)

#     return s
# print(sum_list(L))
# def sum_list(l):
#     sum1=sum(emm(L))
#     return sum1

# print(sum_list(L))

# l=[{s:3,d:4,g:5},{s:4,d:5,g:7}]
# a=l['d']
# print(a)