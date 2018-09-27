#def  info(name ,age=1,address="xian"):
#    print("我叫",name,"住在",address,"今年",age,"岁")
#
#info("xiixi")
#info("ixi","12","大内")
#info("babb",address="15lou")



#a=0
#while a<10:
 #   a=a+1
  #  print("哈哈")



#a=0
#while a<10:
#    a=a+1
#    if a !=7:
#        print(a)
    
#    else:
#           pass



#for a in range(1,10):
#    if a==7:
#        pass
#   else:
#        print(a)
    
#
#s=str(input("请输入："))
#if s[:]==s[::-1]:
#    print("yes")
#else:
#    print("no")


for i in range(100,999):
   if int(i[2])**3+int(i[1])**3+int(i[0])**3==int(i):
       print("yes")





#import time
#from math import factorial as fac
#import math
#a=int(input("shuru:"))
#print(fac(a))
#print(math.factorial(a))


#import time

#while True:
 #   t=time.localtime()
  #  print("\r%02d-%02d-%02d %02d:%02d:%02d"\
   #     %(t[0],t[1],t[2],t[3],t[4],t[5]),end="")
    #time.sleep(02)


#import time
#year=int(input("年份："))
#month=int(input("月份:"))
#day=int(input("日："))

#t=(year,month,day,0,0,0,0,0,0)
#shenri=time.mktime(t)     #生成时间元组  
#now=time.time()             #h获取当前时间

#age=(now - shenri)/60/60/24       #现在的时间减去生日除分秒月天  
#print("你已经出生了%f天了，还不奋斗吗？"%age)
#%f浮点型数据替换输出



#import random as R
#a=R.randint(1,100)
#x=6

#while x!=0:
#    s=int(input("请输入一个数字："))
#    x=x-1
#    if a>s:
#        print("你猜小了，还剩%d机会！"%x) 
#    elif a<s:
#        print("你猜大了，还剩%d机会"%x)
#    else:
#        print("你猜对了")
#        break 


# import random
# #将四个花色放到ｈｕａｓｅ的列表
# huse=["\u2660","\u2663","\u2665","\u2666"]

# number=[str(x) for x in range(2,11)]#生成一个２到１１的随机字符串
# number+=["J","Q","K","A"]# 在数字中加入四个JQKA
# kings=["大王","小王"]
# L=[x+y for x in huse for y in number]#X在huse 循环一次，Ｙ在ｎｕｍｂｅｒ循环一次
# L+=kings

# random.shuffle(L)
# print("第一家牌",L[0:17])
# print("第二家牌",L[17:34])
# print("第三家牌",L[34:51])
# print("底牌",L[51:])
#     
