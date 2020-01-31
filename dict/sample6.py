# 处理员工数据
source ="7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$369,SMITH,ANALYYST,RESEARCH,2000"

employee_list = source.split("$")
print(employee_list)

# 保存所有解析后的员工信息，key是员工编号，value是包含完整员工信息的字典
all_emp = {}

for i in range(0,len(employee_list)):
    # print(i)
    e = employee_list[i].split(",")
    print(e)

#     创建员工字典
    employee = {"no": e[0], 'name': e[1], 'job': e[2], 'department': e[3],'salary': e[4]}
    print(employee)
    all_emp[employee['no']] = employee #这个厉害了

print(all_emp)

