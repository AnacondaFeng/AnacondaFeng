# datetime时间转换
from datetime import datetime, date, time, timedelta

# 自定义日期时间
d = datetime(2020, 10, 30, 14, 5)
print(d)

d2 = date(2019, 3, 23)
print(d2)

t = time(9, 0)
print(t)

print('==========================================')

# 日期时间转换
ds = '2018-10-3 13:42:09'
ds_t = datetime.strptime(ds, '%Y-%m-%d %H:%M:%S')
print(ds_t)

ds_q = '2018/10/3T13:42:09'
ds_t_q = datetime.strptime(ds_q, '%Y/%m/%dT%H:%M:%S')
print(ds_t_q)

# datetime转换成字符串
n = datetime.now()
n_str = n.strftime('%Y/%m/%dT%H:%M:%S')
print(n_str)

print('==========================================')

# datetime加减操作
n = datetime.now()
print(n)

n_next = n + timedelta(days=5, hours=42)
print(n_next)

# 时间的减法
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)

rest = d2 - d1
print(rest)
print(type(rest))
print(dir(rest))
print(rest.days)
print(type(rest.days))