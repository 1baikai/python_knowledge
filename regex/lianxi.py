import re
pattern = r'\s+'
string = 'asssasddd fgahasjk lqw ertyui o657pzx a sdddcvb nm,.'
regex = re.compile(pattern)
x = regex.findall(string)
y = regex.split(string)
z = regex.sub('#',string,2)
q = regex.subn('123',string,2)
print(x)
print(y)
print(z)
print(q)