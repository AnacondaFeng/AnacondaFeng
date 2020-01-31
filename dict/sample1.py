employee = {'name': 'wangfeng', 'salary': 1000, 'job': 'sales'}

# 字典取值

name = employee['salary']
print(name)

print(employee.get('job'))

# in 成员运算符
print('name' not in employee)

# 遍历字典
for key in employee:
    v = employee[key]
    print(v)

for k, v in employee.items():
    print(k, v)
