import re

s = 'one1two2three333four4five5six6'
"""正则表达式替换"""

p = re.compile(r'\d+')
rest = p.sub('@', s)
print(rest)

"""更换位置"""
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')

rest_pos = p2.sub(r'\2 \1', s2)
print(rest_pos)

"""替换改变内容"""


def f(m):
    return m.group(2).upper() + ' ' + m.group(1)


rest_change = p2.sub(f, s2)
print(rest_change)

"""匿名函数lambda"""
rest_lamb = p2.sub(lambda m: m.group(2).upper() + ' ' + m.group(1), s2)
print("******************************")
print(rest_lamb)
