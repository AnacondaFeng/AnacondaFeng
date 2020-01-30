a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]
# 求两个列表之间的交集
int_list = list(set(a_list).intersection(set(b_list)))
print(int_list)
# 求两个列表之间的并集
uni_list = list(set(a_list).union(set(b_list)))
print(uni_list)
# 求两个列表之间的差集（a_list在b_list中不存在的部分）
dif_list = list(set(a_list).difference(set(b_list)))
print(dif_list)

# 集合间的关系操作
s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 5, 4, 3, 2, 1}

# ==判断两个集合的元素是否完全相同
print(s1 == s2)

s3 = {4, 5, 6, 7}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}
print(s3.issubset(s4))
# 判断是否为子集
print(s4.issuperset(s3))
# 判断是否为父集

s5 = {5}
s6 = {1, 3, 5, 7, 9}
s5.isdisjoint(s6)
# 判断是否存在重复元素，True代表不存在
