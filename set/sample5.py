# 生成式

lst1 = []
for i in range(10, 20):
    lst1.append(i * 10)
print(lst1)

# 列表生成式
lst2 = [i * 10 for i in range(10, 20)]
print(lst2)

lst3 = [i * 10 for i in range(10, 20) if i % 2 == 0]
print(lst3)

lst4 = [i * j for i in range(1, 5) for j in range(1, 5)]
print(lst4)

# 字典生成式
lst5 = ['张三', '李四', '王五']
dict1 = {i + 1: lst5[i] for i in range(0, len(lst5))}
print(dict1)

# 集合生成式
set1 = {i * j for i in range(1, 4) for j in range(1, 4) if i == j}
print(set1)


lst = [23, 45, 22, 44, 25, 66, 78]
# 生成所有奇数组成的列表
lst1 = [i for i in lst if i%2 != 0]
print(lst1)
# 输出结果[28, 50, 27, 49, 30, 71, 83]

#print(lst2)