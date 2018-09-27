# 3. 生成前40个斐波那契数(Fibonacci)
#   1 1 2 3 5 8 13 21 ......
#   要求将这数整数存于列表L中,最后打印出这些数
#   (斐波那契的前两个是1, 1, 之后的数是前两个数的和)

L = []  # 准备放入数据

# 方法1
#L = [] 
# a = 0
# b = 1  # 当前已经求出来的数
# while len(L) < 40:  # 不够40个
#     L.append(b)  # 把已经得到的数加入列表中
#     # 再算出下一个数,依旧存于b中,为下次循环做准备
#     c = a + b  # 下一次的数
#     a = b  # 将当前的数交给a
#     b = c  # 再把已经算好的数交给b

# 方法2
#L = [] 
# a = 0
# b = 1  # 当前已经求出来的数
# while len(L) < 40:  # 不够40个
#     L.append(b)  # 把已经得到的数加入列表中
#     # 再算出下一个数,依旧存于b中,为下次循环做准备
#     a, b = b, a + b

# 方法3
L = [1, 1]
while len(L) < 40:
    L.append(L[-1] + L[-2])

print(L)



