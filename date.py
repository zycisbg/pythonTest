from datetime import datetime

now = datetime.now()

print(now)

dt = datetime(2015, 5, 12, 12, 33, 22)

print(dt)

# timestamp 和 datetime 转换
dt = dt.timestamp()

print(dt)

dt = datetime.fromtimestamp(dt)

print(dt)

# datetime 和 str 转换

date = datetime.strptime('2017-10-11 12:12:12', '%Y-%m-%d %H:%M:%S')

print(date)


print(date.strftime('%Y-%m-%d %H:%M:%S'))
