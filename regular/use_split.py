import re

s = 'one1two2three333four4five5six6'

"""使用split分割"""
p = re.compile(r'\d+')
rest = p.split(s, 2)
print(rest)
