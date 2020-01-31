# 集合的遍历
college1 = {"哲学", "经济学", "法学", "教育学"}

for c in college1:
    print(c)

# 判断元素存在
print("哲学" in college1)
print("计算机学" in college1)

# 集合不支持按索引提取数据

# 新增数据
college1.add("计算机学")
college1.add("法学")

print(college1)

# update一次添加多个元素
college1.update(["生物学", "工程学"])
print(college1)

# 不支持更新，先删除再添加
college1.remove("生物学") #如果删除不存在的元素，会报错

college1.discard("生物") #如果元素不存在，忽略
college1.add("医学")
print(college1)


