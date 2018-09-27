def get_yh_list(n):
    L = []
    line = [1]
    for   in range(n):
        L.append(line)    

        line = get_next_line(line)
    return L
def get_next_line(l):
#此函数将用一层的列表l计算下一层然后返回
#如：l = [1,3,3,1],则返回:[1,4,6,4,1]
    line = [1] #最左边的
    #计算中间的数字
    for i in range(len(l)-1): #i绑定l的索引
        line.append(l[i]+l[i+1])
    #在最后放入一个１
    line.append(1)
    return line
def get_char(L):
#此函数任意给定一个列表，将其转换为字符串
#如：l = [1,3,3,1],则返回'1 3 3 1'    
    l2 = [str(x) for x in L]
    return ' '.join(l2)
#得到最下面一行站几个字符的宽度：
max_char = len(list_to_string(l[-1]))
L = get_yh_list(6)
print(L)
#居中显示
for line_list in L:
    s = list_to_string(line_list)
    print(s.center(max_char))