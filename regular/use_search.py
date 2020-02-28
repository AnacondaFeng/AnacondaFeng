import re

content = 'hello, world！'

p = re.compile(r'world')
# 使用search
rest = p.search(content)
print(rest)

# match使用的时候从一开始就找，没找到就不找了
rest = p.match(content)
print(rest)