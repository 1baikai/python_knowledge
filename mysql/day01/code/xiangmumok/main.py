import student_info 
import menu 
def main():
    a="1"
    b="2"
    c ='3'
    d="4"
    f ="5"
    g="6"
    h="7"
    k="8"
    a1="9"
    a2="E"
    e='q'
    L=[]
    while True:
        x=input("请选择：")

        if x is a:
            L=L+student_info.input_student(L)
            print(L)
        elif x is b:
            student_info.output_student(L)
        elif x is c:
            student_info.delete_student(L)
        elif x is d:
            student_info.correct_student(L)
        elif x is f:
            L=sorted(L,key=student_info.cj,reverse=True)
            student_info.output_student(L)
        elif x is g:
            L=sorted(L,key=student_info.cj,reverse=False)
            student_info.output_student(L)
        elif x is h:
            L=sorted(L,key=student_info.nj,reverse=True)
            student_info.output_student(L)
        elif x is k:
            L=sorted(L,key=student_info.nj,reverse=False)
            student_info.output_student(L)
        elif x is a1:
            student_info.cun(L)
        elif x is a2:
            student_info.read(filename='si.txt')
            


        else:
            x is e
            break
main()