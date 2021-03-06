# try_except.py


# 此示例示意try-except语句中　as 变量的用法
def div_apple(n):
    print("%d个苹果您想分给几个人?" % n)
    s = input('请输入人数: ')
    cnt = int(s)  # <<- 可能触发ValueError错误进入异常
    result = n / cnt  # <<-- 可能触ZeroDivisionError错误
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果完成")
except ValueError as err:
    print("错误值是: ", err)  # err绑定错误对象

print("程序正常退出")






