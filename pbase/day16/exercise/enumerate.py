numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for t in zip(numbers, names):
    print(t)
for No, number, name in zip(range(1, 100),
                              numbers,
                              names):
    print("序号",No, name, '的客服电话是:', number)



names = ['中国移动', '中国电信', '中国联通']

for t in enumerate(names):
    print(t)  #(0, '中国移动')(1, '中国电信')(2, '中国联通')
for t in enumerate(names, 101):
    print(t)  #(101, '中国移动')(102, '中国电信')