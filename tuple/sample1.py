# 元组是不可变的列表

tup = ('physics', 'chemistry', 1997, 2000)

# 元组的读写操作

tup1 = (5, 6, 7)
tup2 = (8, 9, 10)

tup3 = tup1 + tup2 * 2
print(tup3)
print(type(tup3))

# 获取数据
print(tup3[5])
print(tup3[-1])
print(tup3[1:4])

# 元組運算符
t3 = (1, 2, 3) + (4, 5, 6)
print(t3)

t4 = (10,) * 5  # 元组只有一个元素时，必须增加逗号
print(t4)
