# datetime标准模块
import datetime
# from datetime import datetime

import time

print(dir(datetime))

print("now:{0}".format(datetime.datetime.now()))

now_time = datetime.datetime.now()

# 当前日期
print('now day:{0}'.format(now_time.date()))

# 当前时间
print('now time:{0}'.format(now_time.time()))

print('now day2:{0}'.format(datetime.datetime.today()))

print('year:{0}'.format(now_time.year))

print('month:{0}'.format(now_time.month))

print('day:{0}'.format(now_time.day))

print(dir(now_time))

print('weekday:{}'.format(now_time.weekday()))

print(time.time())  # 获取毫秒数

time.sleep(2)
