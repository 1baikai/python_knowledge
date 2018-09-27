# try:
#     L=[]
#     f=open('info.txt','r')
#     b=f.readlines()
#     for i in b:
#         s=i.strip()
#         name, age, score = s.split() 
#         age = int(age)  # 转为整数
#         score = int(score)
#         L.append({'name':name,'age':age,'score':score})
#         # L.append(s)
#     print(L)
#     # a=b.decode('utf-8')

#     print("打开")
#     # print(a)
#     f.close()
# except:
#     print("打开失败")


def write():
    L=[]
    while True:
        x=input("请输入：")
        if not x:
            break
        L.append(x)
    return L
def seve(L):
    try:
        fw=open('lalla.txt','w')
        for i in L:
            fw.write(i)
            fw.write('\n')
        fw.close()
    except:
        print("打开失败")
def read(filename='lalla.txt'):
    l=[]
    try:
        fr=open(filename,'r')
        b=fr.readlines()
        for i in b:
            a=i.strip()
            l.append(a)
        fr.close()
    except:
        print("couo")
    return l
def print_text(l):
    for line_number, s in enumerate(l, 1):
        print(line_number, ":", s)





L=write()
seve(L)
read('lalla.txt')

if __name__ == '__main__':
    print_text(read())
