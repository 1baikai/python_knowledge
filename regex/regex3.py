import re
s= '''hallo world
hello kitty
您好'''

pattern = r'^he'

regex = re.compile(pattern,flags=re.M)

try:
    x = regex.search(s).group()
except:
    print(' 没有匹配到')
else:
    print(x)