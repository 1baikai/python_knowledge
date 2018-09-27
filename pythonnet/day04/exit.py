import os,sys

#结束进程后不再执行后面内容

# os._exit(0)
try:

    sys.exit("123124")
except SystemError as e:
    print("退出",e) 
print("process exit")