def input_student():
    L=[]
    while True:
        d={}
        x=str(input("请输入姓名："))
        if x =="":
            break
        try:
            y=int(input("请输入年龄："))
            if 0<=y<=100:
                y=y
            else:
                return 0
        except ValueError:
            return 0
        try:
            z=int(input("请输入成绩："))
            if 0<=z<=100:
                z=z
            else:
                return 0
        except ValueError:
            return 0

        d['name']=x
        d['age']=str(y)
        d['score']=str(z)
        L.append(d)
    return L
print(input_student())