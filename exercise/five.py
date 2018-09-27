def main():

    file = str(input("请输入你要显示的表："))
    print("**********************************************")
    print("*                 第"+"1"+"周期                    *")
    print("**********************************************")
    print('<'+'name'.center(20)+'><'+'work'.center(10)+'><'+'money'.center(10)+'>')
    
 
    f=open(file,'r')
    while True:
        s=f.readline()
        if not s:
            break
        x=s.strip().split(' ')
        name=x[0]
        work=x[1]
        money=x[2]
        print('*',name.center(18),'*',work.center(8),'*',money.center(8),'*')


    f.close()
    print("**********************************************")
main()

