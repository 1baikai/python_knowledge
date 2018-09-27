import re
it = re.finditer(r'\d+','豆腐花黑人哦符合欧尼违反欧豪额然后我　我；偶尔会123jsdfn23446')

for i in it :
    print(i.group())

try:
    obj = re.fullmatch(r'\w+','asdfasgfwq32&')
    print(obj.group())
except AttributeError as e:
    print(e)

ibj = re.match(r'foo','foo,food on jasdj')
print(ibj.group())


ibj = re.search(r'foo','foo,food on jasdj')
print(ibj.group())