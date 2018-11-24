#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月24日

@author: zzk
'''
# 获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now,type(now))
# 注意到datetime是模块，datetime模块还包含一个datetime类，
# 通过from datetime import datetime导入的才是datetime这个类。

# 获取指定日期和时间
dt = datetime(2018,11,24,19,59,35,65)
print(dt)
# datetime转换为timestamp
print(dt.timestamp())
#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# timestamp转换为datetime
print(datetime.fromtimestamp(dt.timestamp()))
# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
# 上述转换是在timestamp和本地时间做转换。
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(dt.timestamp()))
print('---------------')

# str转换为datetime
cday = datetime.strptime('2018-6-1 18:16:59','%Y-%m-%d %H:%M:%S')
print(cday,cday.timestamp(),type(cday))
# datetime转换为str
cdayStr = cday.strftime('%Y-%m-%d %H:%M:%S')
print(cdayStr)
print('---------------')

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import timedelta
now = datetime.now()
print(now+timedelta(hours=2),now-timedelta(minutes=16))

# 本地时间转换为UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
print('-------------')
# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow()
print('utc时间:',utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间:',bj_dt)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。