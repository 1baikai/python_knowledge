import re

f = open('test.txt')

pattern = r'[A-Z]\w*'
l = []

for line in f:
    l += re.findall(pattern,line)

f.close()
print(l)