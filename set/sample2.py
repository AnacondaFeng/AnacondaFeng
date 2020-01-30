college1 = {'123', '456'}

college2 = {'456', '789'}

# 交集
c3 = college1.intersection(college2)

college1.intersection_update(college2)

print(college1)

# 并集
college1 = {'123', '456'}

college2 = {'456', '789'}

c4 = college1.union(college2)
print(c4)

# 差集
college1 = {'123', '456'}

college2 = {'456', '789'}

c5 = college1.difference(college2)
print(c5)

c6 = college1.symmetric_difference(college2)