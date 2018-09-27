# one.py
#1. 编写一个程序，它以球的半径（浮点数）作为输入，
#   并且输出球体的直径，圆周长，表面积和体积

# from math import pi

# def qiu():
#     r = float(input("请输入球的半径："))
#     d = 2 * r
#     c = pi * d
#     s = 4 * pi * r **2
#     v = 4 /3 * pi * r **3
#     return d,c,s,v
# print(qiu())

#2. 一个员工的总工资，等于每小时的薪水＊一周的工作时间＋加班费．加班费是加班总时间
#    乘以每小时工资的１．５倍．
# t为总加班时间，m为每小时多少钱
# def money():
#     t=float(input("请输入您的加班时间："))
#     m=float(input("请输入您每小时的薪水："))
#     emolument = 8*5*m+t*(1.5*m)
#     return emolument
# print("周薪水为:",money())



#球的弹跳距离：弹性度为０．６．
# def h(n,s):
#     if n ==0:
#         return s
#     for i in range(1,n+1):
#         s=s*0.6
#     return s

# def sum(n):
#     sum1=0
#     for i in range(0,n):
#         sum1=sum1+h(i,s)+h(i+1,s)
#     return sum1

# n = int(input("请输入弹跳几次："))
# s = float(input("初始高度:"))
# print(sum(n))




# pi/4=1-1/3+1/5-1/7....

# def xiang(n):
#     a = (-1)**n / (2*n+1)
#     return a 
# def so(n):
#     s=[]
#     for i in range(n+1):
#         s.append(xiang(i))
#     return s 
# n = int(input("前几项"))
# print(sum(so(n)))


