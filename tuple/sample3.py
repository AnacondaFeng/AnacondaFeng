count = 0
# 定义一个空列表用于存放数据
lst = []
for i in range(1, 5):
    # 使用for循环得到另一个数j
    for j in range(1, 5):
        if i != j:
            # 将数据添加到列表中
            lst.append(str(i) + str(j))
            count += 1
print(count)
# 输出得到的数据
print(lst)

