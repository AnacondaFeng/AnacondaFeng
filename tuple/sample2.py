# 序列

# 数据结构包含四种
# 1.字符串 str
# 2.列表 list
# 3.元组 tuple
# 4.数字序列 range

r1 = range(0, 100)
print(r1)
print(r1[4:9])
print(r1[29])

# 增加步长
r2 = range(10, 20, 2)
print(r2)  # 10 12 14 16 18

print(12 in r2)
