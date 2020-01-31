# 1.序列传参
def calc(a, b, c):
    return (a + b) * c


l = [1, 5, 10]

# print(calc(1, 5, 10))
print(calc(*l))


# 2.字典传参
def health_check(name, height):
    print("111")


param = {"name": "张三", "height": 180}

health_check(**param)


# 3.返回值包含多个数据
def get_detail_info():
    dict1 = {
        "employee": [{"name": "张三", "salary": 1800},
                     {"name": "李四", "salary": 2000}],
        "device": [{}, {}]
    }
    return dict1


print(get_detail_info())

d = get_detail_info()
print(d.get("employee")[0])
