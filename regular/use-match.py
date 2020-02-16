import re

# 编译成正则表达式对象
pattern = re.compile(r'Hello', re.I)

# 通过match进行匹配
rest = pattern.match('hello,world!')
print(rest)
print(type(pattern))
print(dir(pattern))