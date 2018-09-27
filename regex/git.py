# import re 


# １打开文件
# 每一段  r'\r\n\w+$'

import re
import sys

def main():
    if len(sys.argv)<2:
        print('输入端口名字')
    name = sys.argv[1]
    f = open('1.txt')

    pattern = r'\r\n\w+$'
    l = []

    string = f
    print(string)

    l += re.findall(pattern,string)

    f.close()
    print(l)