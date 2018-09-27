import re
pattern = r'(ab)cd(ef)'
s = "abcdefghjilkophioabababcdefefk"
l = re.findall(pattern,s)
print(l)

print("++++++++++++++++++++++++++++++++++++++++")

regex = re.compile(pattern)
l = regex.findall(s)
print(l)

print("++++++++++++++++++++++++++++++++++++++++")

l = re.split(r'\s+','hello world nihao lalal')
print('split():',l)

print("++++++++++++++++++++++++++++++++++++++++")

s = re.sub(r'\s+','#','hello  ik nihao china lal',3)
print('sub():',s)

print("++++++++++++++++++++++++++++++++++++++++")


s = re.subn(r'\s+','#','hello  ik nihao china lal',3)
print('sub():',s)
