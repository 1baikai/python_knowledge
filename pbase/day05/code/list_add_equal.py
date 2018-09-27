
# 列表是可变的对象, += 是修改原来的对象
x = [1, 2, 3]
print(id(x))  # 139805087766920
x += [4, 5, 6]
print(id(x))  # 139805087766920

# 字符串是不可变的对象 += 是创建新的对象,让变量绑定新的对象
# sx += "123" 等同于 sx = sx + '123'
sx = "ABC"
print(id(sx))  # 139805112114904
sx += "123"  # sx = 'ABC123'
print(id(sx))  # 139805080811480