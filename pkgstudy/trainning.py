from datetime import datetime, time as t1, timedelta
import time

# 得到当前日期时间（两种方法）
print(datetime.now())
print(datetime.today())
# 得到当前日期
print(datetime.now().day)
# 得到当前时间
print(datetime.now().time())
# 得到当前年份用year_变量接收
year_ = datetime.now().year
# 得到当前月份用month_变量接收
month_ = datetime.now().month
# 得到当前天用day_变量接收
day_ = datetime.now().day
# 使用-拼接年月日得到当前日期
print('{y}-{m}-{d}'.format(y=year_, m=month_, d=day_))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# import datetime, time

# 自定义日期时间为2019-10-10 8:10
date_time = datetime(2019, 10, 10, 8, 10)
# 打印自定义的日期时间对象
print(date_time)
# 使用time模块的sleep函数停顿2秒
time.sleep(2)
# 自定义日期2019-11-11
date_ = datetime(2019, 11, 11)
# 打印自定义的日期对象
print(date_)
# 自定义时间11:11
time_ = t1(11, 11)
# 打印自定义的时间对象
print(time_)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# from datetime import datetime
# 定义一个str_字符串为2019-09-10 8:10:56
str_ = '2019-09-10 8:10:56'
# 将str_转换为日期函数2019-09-10 8:10:56
str_date = datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
print(str_date)
# 定义now_变量接收当前的日期时间
now_ = datetime.now()
# 将当前日期时间格式化为——四位的年份/月/日 时:分:秒
date_str = datetime.strftime(now_, '%Y/%m/%d %H:%M:%S')
print(date_str)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 定义now_变量接收当前日期时间
now_ = datetime.now()
# 计算距当前日期时间3天36小时12分钟之前的日期时间
now_before = now_ - timedelta(days=3, hours=36, minutes=12)
# 计算10天之后的日期时间
now_after = now_ + timedelta(days=10)
print(now_before)
print(now_after)
