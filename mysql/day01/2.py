# #装饰器
# def mydeco(fn):#<----装饰器函数
#     def fx():
#         print("fx被调用")
#     return fx

# # @mydeco
# def myfun():


#     print("myfun被调用")

# #上述mydeco的原理是def myfun语句调用之后加了如下语句
# myfun=mydeco(myfun)

# myfun()#调用myfun
# myfun()
# myfun()
# #改写装饰器
# #此实例示意装饰器函数用来包装被装饰函数
# def mydeco(fn):#<----装饰器函数
#     def fx():
#         print("－－－这是被装饰函数调用之前")
#         fn()#调用被装饰函数
#         print("＋＋＋这是被装饰函数调用之后")
#     return fx

# @mydeco
# def myfun():


#     print("myfun被调用")

# myfun()#调用myfun
# myfun()
# myfun()


#闭包：
#此示例示意装饰器的应用场合及功能
#---------------------------
# def privileged_check(fn):
#     print("ssss")#buhui
#     def fx(name,x):
#         print('正在进行权限验证')
#         if True:
#             fn(name,x)
#         else:
#             print('权限验证失败')
#     return fx



# #---------------------------
# @privileged_check
# def savemoney(name,x):

#     print(name,'存钱',x,'元')
# # @privileged_check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
# #----------------------------
# savemoney('校长',200)
# savemoney("小赵",500)


# withdraw('小红',400)

#######################################
# def privileged_check(fn):
#     print("ssss")#调用装饰器
#     def fx(name,x):
#         print('正在进行权限验证')
#         if True:
#             fn(name,x)
#         else:
#             print('权限验证失败')
#     return fx



# #---------------------------
# @privileged_check
# def savemoney(name,x):

#     print(name,'存钱',x,'元')
# # @privileged_check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
# #----------------------------
# savemoney('校长',200)
# savemoney("小赵",500)


# withdraw('小红',400)

# L=[1,2,3]
# def f(n=0,lst=[]):
#     lst.append(n)
#     return lst
# print(f(4,L)) #1,2,3,4,
# print(f(5,L)) #1,2,3,5
# f(100)   #[100]
# f(200)  #[200]


# import math as m
# x=float(input("请输入半径"))
# s=(m.pi)*m.pow(x,2)
# print(s)
# n=float(input("请输入面积："))
# r=m.sqrt(n/m.pi)
# print(r)

# print("kaishi")
# import time
# time.sleep(10)
# print("jiehsu")

# 写一个程序，，输入你的出生日期
# １）算出你已经出生了多少天？
# ２）算出你出生那天是星期几？＼
# import time
# year=int(input("年份："))
# month=int(input("月份:"))
# day=int(input("日："))

# t=(year,month,day,0,0,0,0,0,0)
# shenri=time.mktime(t)     #生成时间元组  
# now=time.time()             #h获取当前时间

# age=(now - shenri)//60//60//24       #现在的时间减去生日除分秒月天  
# print("你已经出生了%f天了，还不奋斗吗？"%age)
# t=time.localtime(shenri)
# week={0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期天"}
# print("出生那天是",week[t[6]])

#写一个程序，打印电子时间：
#格式为：ＨＨ：ＭＭ：ＳＳ　　每过一秒刷新一次
# import time
# while True:
#     a=time.time()
#     b=time.sleep(1)
#     c=time.localtime(a)
#     hh=c[3]
#     mm=c[4]
#     ss=c[5]
#     print(hh,':',mm,":",ss)
#laosizuode 
# import time
# while True :

#     t= time.localtime()
#     # print("%02d:%02d:%02d"%(t[3],t[4],t[5]))
#     print("%02d:%02d:%02d"%t[3:6],end='\r')
#     time.sleep(1)

#编写一个闹钟程序，启动时设置定时间，到时间后打印＂时间到，然后退出

# import time
# shi=int(input("请输入小时"))
# fen=int(input("请输入分"))
# miao=int(input("请输入秒"))
# while True:
#     a=time.time()
#     b=time.localtime(a)
#     time.sleep(1)
#     if shi==b[3] and fen==b[4] and miao==b[5]:
#         print("时间到！！！！")
#         break 


#lasohi zuode 
# import time
# def alarm(h,m):
#     while True:
#         #得到当前时间
#         t=time.localtime()
#         print("%02d:%02d:%02d"%t[3:6],end='\r')
#         if h==t[3] and m==t[4]:
#             print("\n时间到")
#             break
#         time.sleep(1)
# hour=input("请输入定时小时：")
# minute=input("请输入定时分钟：")
# alarm(hour,minute)



# 函数装饰器，适用不想改变原函数的名字，还想在原基础上在添加新的功能就是装饰器。
# 原函数写的很复杂很好，别人就只记得这个函数名字。为了不去改原函数，才出现装饰。
# 这个原函数不一定只是你用，用的功能也不一定一样，所有把原函数拿过来自己装饰成合适自己的。

# def haha(x):
#     def shi():
#         # print("**********")
#         # print("----------")
#         print("++++++++++") 
#         x()
#         print("++++++++++")
#         # print("----------") 
#         # print("**********")     #装饰（装饰器函数）
#     return shi
# # @haha  

# def xixi():
#     print("hello tarena")
#     print("hello mary") 
# xixi=haha(xixi)          #被装饰（原函数） 
# xixi()


# import sys
# print('kaskjks')
# sys.exit(0)

# print('askj')

# import mymod
# mymod.myfac(5)
# mymod.mysum(1000)
# print(mymod.name1)


# import random
# x=int(random.uniform(1,100))
# i=0
# while True:
    
#     y=int(input("请输入一个数字"))
#     i=i+1
#     if y==x:
#         print("小逼崽子猜对了！厉害呢！")
#         print("小逼崽子猜了%d次"%i)
#         break
#     elif y<x:
#         print("小逼崽子猜小了")
#     else:
#         print("小逼崽子猜大了")


#模拟斗地主发牌，共５４张，黑桃（＇＼u２６６０＇）梅花　方块　红桃
#Ａ２－１０jqk,大王　小王
#3个人　　一个人17，底牌３张
#回车，第一个人
#回车，第一个人
#回车，第一个人
# import random
# huase=["\u2660","\u2666","\u2667","\u2661"]
# a=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
# L=[]
# wang=['大王','小王']
# for x in huase:
#     for y in a:
#         new=x+' '+y
#         L.append(new)

# newL=L+wang
# random.shuffle(newL)
# one=input("")
# for diyi in newL[0:17]:
#     print (diyi,end=' ')
# two=input("")
# for dier in newL[17:34]:
#     print (dier,end=' ')
# san=input("")
# for disan in newL[34:51]:
#     print (disan,end=' ')
# si=input("")
# for disi in newL[51:54]:
#     print (disi,end=' ')
# one=input("")

# print("第一家牌",newL[0:17])
# two=input("")
# print("第二家牌",newL[17:34])
# san=input("")
# print("第三家牌",newL[34:51])
# si=input("")
# print("底牌",newL[51:])

#99乘法表
# def jiujiu():
#     for a in range(1,10):
#         for b in range(1,10):
#             print(b,"*",a,"=",(a*b),end=" ")
#             if a==b:
#                 break
#         print() 

# jiujiu()


# def div_apple(n):
#     print("%dgepingguo nixiangfengeijigeren ?"%n)
#     s=input('qingshuru jigerne ')
#     cnt=int(s)
#     result=n/cnt
#     print("meiyige fenl ",result,'ge pingguo' )
# try:
#     div_apple(10)
#     print("fenpingguowancheng ")
# except ValueError:
#     print("zai  try  De neibuyujuzhongfashenglezhicuowu,yichuli ")
# print("chengxuzhengcahngtuichu ") 

# def get_score():
#     score=int(input("请输入成绩："))
#     if 0<=score<=100:
#         return score
#     else:
#         return 0
# try:     
#     score=get_score()
#     print("学生的成绩是：",score)
# except ValueError:
#     print(0)

# fangfa2
# def get_score():
#     try:
#         score=int(input("请输入成绩："))
#     except ValueError:
#         return 0
#     if 0<=score<=100:
#         return score
#     else:
#         return 0
# score=get_score()
# print("学生的成绩是：",score)

# def fry_egg():
#     print("打开天然气．．")
#     try :
#         count=int(input("请输入鸡蛋个数"))
#         print("完成剪辑但，共建了%d个鸡蛋"%count)
#     finally:
#         print("关闭天然气")
# try:
#     fry_egg()
# except ValueError:
#     print("程序出现异常，已恢复正常")

# print("程序正常退出")

# try:
#     try:
#         n=int(input("请输入整数"))
#     except ValueError:
#         print("在内层try语句内出现值错误，一转为正常转台")
#     else:
#         print("内层try语句没有出现异常")
# except:
#     print("外层的try语句接收到异常通知，已处理并转为正常状态")
# else:
#     print("外层try语句没有出现异常")

# def make_except():
#     print("kaishi")
#     # raise ValueError  #故意发送一个错误通知
#     e=ValueError("zhehsiguyi zhizuo de yige cuowutongzhi")
#     raise e
#     print("jieshu")
# try:
#     make_except()
# except ValueError as err:
#     print("make_except发出了类型错误，已捕获")
#     print("cuowude zhi shi ",err)
# print("chengxujieshu")


# def make_except():
    
#     raise ValueError ("wode 一个值错误") #故意发送一个错误通知
#     e=ValueError("zhehsiguyi zhizuo de yige cuowutongzhi")
# def get_except():

#     try:
#         make_except()
#     except ValueError as err:
#         print("cuowude zhi shi ",err)

# try :
#     get_except()
# except ValueError as err:
#     print("get_except内部发了错误")
# print("chengxujieshu")

# def get_age():
#     a=int(input("请输入年龄："))
#     if 1<=a<=140:
#         return a
#     else:
#         raise ValueError("值不在１～１４０之间")
# try:
#     age=get_age()
#     print("用户输入的年龄是",age)
# except ValueError as err:
#     print("用户输入的不是１～１４０的整数，获取年龄失败")

# def get_score():
#     s=int(input("请输入学生成绩（0～１００）"))
#     # assert 0<=s<=100,'成绩超出范围'
#     #等同于：
#     if (0<=s<=100)==False:
#         raise AssertionError('成绩超出范围')
#     return s


# try:
#     score = get_score()
#     print("学生的成绩：",score)
# except ValueError:
#     print("用户输的数字不能转为整数")
# except AssertionError:
#     print("用户输入的整数不再０～１００之间")



# def h(n):
#     if n==0:
#         return 100
#     s=100
#     for i in range(1,n+1):
#         s=s/2
#     return s
# print (h(10))
# def zongchang(n):
#     sum1=0
#     for i in range(0,n):
#         sum1=sum1+(h(i)+h(i+1))
#     return sum1
# print(zongchang(10))


 
# def get_num_factors(num):
 
#     list0=[]
#     tmp=2
#     if num==tmp:
#         print (num)
#     else:
#         while (num>=tmp):
#             k=num%tmp
#             if( k == 0):
#                 list0.append(str(tmp))
#                 num=num/tmp  #更新
#             else:
#                 tmp=tmp+1  #同时更新除数值，不必每次都从头开始
#     print (' '.join(list0)+' ')

# num=int(input())
# get_num_factors(num)
# 分解质因数
# def zhiyinshu():
#     L=[]
#     x=int(input("请输入正整数："))
#     if x<2:
#         print(2)
#     else:
#         i=2
#         while i<=x:
#             if x%i==0:
#                 L.append(i)
#                 x=x/i
                

#             else:
#                 i+=1
#         return L
# print(zhiyinshu())


# s={'唐僧','悟空','八戒','沙僧','白骨精'}
# for x in s:
#     print(x)
# else:
#     print("结束")

# myit=iter(s)
# while True:
#     try:
#         x=next(myit)
#         print(x)
#     except StopIteration:
#         print("程序结束")
#         break


# myit=iter(s)
# try:
#     while True:
#         x=next(myit)
#         print(x)
# except StopIteration:
#     print("遍历结束")

# def myeven(start,stop):
#     i=1
#     while start<stop:
#         start=i*2
#         if start==stop:
#             break
#         yield start
#         i+=1
# for x in myeven(1,10):
#     print(x)

# L=[x ** 2 for x in myeven(2,20)]
# print(L)
# def jc(n):
#     if n==1:
#         return 1
#     return n*jc(n-1)
# def myfactorial(n):
#     i=1
#     while i<=n:
#         yield(jc(n))
# L=list(myfactorial(5))

# def myfactorial(n):
#     s=1
#     i=1
#     while i<=n:
#         s=s*i
#         yield s
#         i=i+1
        
# L=list(myfactorial(5))
# print(L)

# def myfactorial(n):
#     s = 1 #用来保存阶乘
#     for x in range(1,n+1):
#         s *= x
#         yield s
# L = list(myfactorial(5))# L = [1,2,6,24,120]
# print(L)  


# L=[2,3,5,7]
# def gen1(L):
#     for x in L:
#         s=x**2+1
#         yield s
# for x in gen1(L):
#     print(x)

# L=[2,3,5,7]
# gen=((x**2)+1 for x in L)   #for a in (x**2+1 for x in L)
# it=iter(gen)                #    print(a)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# L=[2,3,5,7]
# def gen2(L):
#     for x in L:
#         s=x**2+1
#         yield s
# l=list(gen2(L))
# print(l)

# def nb():
#     l=[]
#     while True:  
#         x=input("请输入：")
#         if not x:
#             break
#         l.append(x)
#     return l
# def aj(a):
#     for t in enumerate(a,1):
#         print("第%d行：%s"%t)

# a=nb()
# print(a)
# aj(a)


# def su(begin,end):
#     if begin<2:
#         pass
#     else:
#         for i in range(begin,end+1):
#             for x in range(2,i):
#                 if i%x==0:
#                     break
#                 else:
#                     continue
#             else:
#                 yield i
# begin=int(input("请输入一个开始数："))
# end=int(input("请输入一个结束数："))
# L = list(su(begin,end))
# print(L)


# def myxrange(start,stop=None,step=1):
    
#     if stop is None:
#         stop=start
#         start=0

#         while start<stop:
#             yield start
#             start+=step
#     if step >0 and start<stop:
#         while start<stop:
#             yield start
#             start+=step
#     elif step<0 and stop < start:
#         while stop<start:
#             yield start
#             start+=step
#     else:
#         yield None

# l=list(myxrange(20))
# print(l)
# l=list(myxrange(1,10))
# print(l)
# l=list(myxrange(1,10,2))
# print(l)
# l=list(myxrange(10,5,-2))
# print(l)
# l=list(myxrange(1,10,-2))
# print(l)

# for a in(x**2 for x in myxrange(1,10,2)):
#     print(a)


def write():
    l=[]
    while True:
        x=int(input("请输入整数："))
        if x <0:
            break
        l.append(x)
    return l 

def cun(l,filename='numbers.txt'):
    try:
        f=open(filename,'w')
        for x in l:
            s=str(x)
            f.write(s)
            f.write('\n')
        print("写入成功")
        f.close()
    except OSError:
        print("写入失败")


l=write()
cun(l)

def read():
    try:
        l=[]
        f=open("numbers.txt",'rb')
        s=f.readlines()
       
        for i in s:
            y=int(i.rstrip())
            l.append(y)
        print(l)
        print(sum(l),max(l),min(l))
        f.close()
    except OSError:
        print("打开失败")
read()

