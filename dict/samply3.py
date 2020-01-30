#字典的更新操作
employee = {'name':'汪峰','sex':'男',
            'hiredate':'1997-10-20','grade':'A',
            'job':'销售','salary':1000,
            'welfare':100
            }

print(employee)
#单个KV更新
employee['grade'] = 'B'
#多个KV更新
employee.update(salary = 1200, welfare = 150)
print(employee)
'''
字典的新增操作，秉承有则更新，无责新增的原则
'''

#删除相关函数
employee.pop('weight')
print(employee)

#popitem删除最后一个kv
kv = employee.popitem()
print(kv)
print(employee)

#clear 清空字典
employee.clear()
print(employee)
