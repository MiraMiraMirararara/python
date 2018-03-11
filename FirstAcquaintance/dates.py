import time  # 引入time模块
import datetime
from datetime import date
ticks = time.time()
print ("当前时间戳为:", ticks)
# dates are easily constructed and formatted

now = date.today()
print(now)
datetime.date(2003, 12, 2)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)