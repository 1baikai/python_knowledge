def main():
    a="1"
    b="2"
    c='3'
    d="4"
    f="5"
    g="6"
    h="7"
    k="8"
    e='q'
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+' '*5+a+')'+'添加学生信息'+' '*23+'|')
    print('|'+' '*5+b+')'+'显示学生信息'+' '*23+'|')
    print('|'+' '*5+c+')'+'删除学生信息'+' '*23+'|')
    print('|'+' '*5+d+')'+'修改学生信息'+' '*23+'|')
    print('|'+' '*5+f+')'+'按学生成绩高－低显示系学生信息'+' '*5+'|')
    print('|'+' '*5+g+')'+'按学生成绩低－高显示系学生信息'+' '*5+'|')
    print('|'+' '*5+h+')'+'按学生年龄高－低显示系学生信息'+' '*5+'|')
    print('|'+' '*5+k+')'+'按学生年龄低－高显示系学生信息'+' '*5+'|')
    print('|'+' '*5+e+')'+'退出'+' '*31+'|')
    print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
    L=[]
    while True:
        x=input("请选择：")

        if x is a:
            L += input_student()
            print(L)
        elif x is b:
            output_student(L)
        elif x is c:
            delete_student(L)
        elif x is d:
            correct_student(L)
        elif x is f:
            L=sorted(L,key=cj,reverse=True)
            output_student(L)
        elif x is g:
            L=sorted(L,key=cj,reverse=False)
            output_student(L)
        elif x is h:
            L=sorted(L,key=nj,reverse=True)
            output_student(L)
        elif x is k:
            L=sorted(L,key=nj,reverse=False)
            output_student(L)

        else:
            x is e
            break