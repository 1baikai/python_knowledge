# 练习:
#   已知有列表:
#     L = [3, 5]
#   用索引和切片操作,将原列表改变为:
#     L = [1, 2, 3, 4, 5, 6]
#   将列表反转,删除最后一个元素后打印此列表
#     ....
#     print(L)  # [6, 5, 4, 3, 2]


# L = [3, 5]
# L[0:0] = [1, 2]  # 把1, 2添加3之前
# L[3:3] = [4]
# L[len(L):] = [6]
# # L[5:] = [6]
# L[::] = L[::-1]  # 先将列表反序生成一个新列表,再替代原列表
# # 此时ID不变
# del L[-1]
# print(L)  # [6, 5, 4, 3, 2]

# 练习:
#   有字符串'hello'请生成'h e l l o'字符串和'h-e-l-l-o'
#   L = list("hello")
#   ' '.join(L)  # ' '.join("hello")  # 'h e l l o'
#   '-'.join("hello")

# s='hello'
# l=list("hello")
# print('-'.join(l))
# 练习:
#   输入一个开始的整数用begin绑定
#   输入一个结束的整数用end绑定
#   将从begin开始,到end结束(不包含end)的所有偶数存于列表中
#   并打印此列表
#   (可以使用列表推导式完成,也可以用循环语句来完成)

# begin=int(input("请输入开始的数字"))
# end=int(input("请输入结束的数字"))
# l=[x for x in range(begin,end) if x %2==0]
# print(l)
# 1. 计算出100以内的素数,将这些素数存于列表中,最后打印出列表中的这些素数
L=[]
while True:
	x=int(input("请输入一个数："))
	if x<0:
		break
	if x< 2 :
		print("不是素数")
	else:
		for i in range(2,x):
			if x%i==0:
				print("不是素数")
				break
		else:
			print("是素数")
			L.append(x)
print(L)

