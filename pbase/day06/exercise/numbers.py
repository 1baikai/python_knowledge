# 练习:
#   写程序,让用户循环输入一些整数,当输入-1时结束输入,
#    将这些整数存于列表L中
#     1) 打印您共输入了多少个有效的数
#     2) 打印您输入的数的最大数是?
#     3) 打印您输入的最小数是多少?
#     4) 打印您输入的这些数的平均值是多少?

# 先创建一个列表:
L = []
while True:
    n = float(input("请输入一些数: "))
    if n == -1:
        break
    L += [n]  # L[len(L):] = [n]

print('您共输入了%d个数' % len(L))
print('您刚才输入的最大数是:', max(L))
print('您刚才输入的最小数是:', min(L))
print('平均数是: ', sum(L) / len(L))






