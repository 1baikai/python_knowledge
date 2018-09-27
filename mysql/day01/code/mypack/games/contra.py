def play():
    print('正在玩魂斗罗...')

def gameover():
    #绝对导入
    #1
    # import mypack.menu
    # mypack.menu.show_menu()
    # #2
    # from mypack.menu import show_menu
    # show_menu()
    # #3
    # from mypack.menu import *
    #x相对导入
    ##1
    # from ..menu import show_menu
    from ..menu import *
    show_menu()






    print("game over!")

print("魂斗罗　　模块被加载")
