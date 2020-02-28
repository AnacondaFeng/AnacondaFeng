import re

# 找出字符串中的数字
content = 'one1two12Three33four444five5six698'

# 编译模式生成个对象
p = re.compile(r'\d+')
rest = p.findall(content)
print(rest)

# 不编译的方式直接用
all_rest = re.findall(r'[a-z]+', content, re.I)
print(all_rest)