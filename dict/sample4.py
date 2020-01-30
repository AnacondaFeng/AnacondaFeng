emp1 = {'name':'Jacky', 'grade':'B'}
emp2 = {'name':'Lily','grade':'A'}

#setdefault为字典设置默认值
emp1.setdefault('grade', 'C')
emp2.setdefault('grade', 'C')
# if 'grade' not in emp2:

print(emp2)

# 获取字典的视图
# 1 keys代表获取所有的键
ks = emp1.keys()
print(ks)
print(type(ks))
# 2 values代表获取所有的值
vs = emp1.values()
print(vs)
print(type(vs))
# 3 items代表获取所有键值对
its = emp1.items()
print(its)
print(type(its))

# 利用字典进行格式化字符串
emp_str1 = "姓名:{name},评级:{grade}".format_map(emp1)
print(emp_str1)

