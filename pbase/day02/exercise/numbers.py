# 练习:
#   输入两个整数,分别用变量 x 和 y绑定
#     1) 计算这两个数的和,并打印结果
#     2) 计算这两个数的积,并打印结果
#     3) 计算x 的 y次方并打印结果
#     如:
#       请输入x : 100
#       请输入y : 200
#     打印如下:
#       100 + 200 = 300
#       100 * 200 = 20000
#       100 ** 200 = ...

x = int(input("请输入x: "))
y = int(input("请输入y: "))
print(x, '+', y, '=', x + y)
print(x, '*', y, '=', x * y)
print(x, '**', y, '=', x ** y)
