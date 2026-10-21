from datetime import datetime, date, time, timedelta, timezone

"""
时间类学习
"""


print("==================================定义时间类==========================================")
now = datetime.now()
d2 = date(2026, 10, 21)
t = time(10, 30, 0)
# 构造时间对象
customer_time = datetime(2026, 9, 20, 11, 30, 00)
print(now)
print(d2)
print(t)
print(customer_time)
print(now.date())
print(now.time())
print(now.month)
print(now.day)


print("==================================时间格式化与解析==========================================")
# 格式化与解析
s1 = now.strftime("%Y-%m-%d %H:%M:%S")
s2 = now.strftime("%Y/%m/%d")          # 2026/10/21
s3 = now.strftime("%A %B %d")          # Wednesday October 21
print(f"时间格式化: {s1}, 时间格式化: {s2}, 时间格式化: {s3}")
print(now.isoformat())                 # 2026-10-21T10:30:15.123456
dt = datetime.strptime("2026-10-21 10:30:00", "%Y-%m-%d %H:%M:%S")
print(f"时间解析: {dt}")

print("==================================时间戳互转==========================================")
# 时间戳互转
print(now.timestamp())
print(int(now.timestamp()))
print(f"{now.timestamp():.0f}")
print(datetime.fromtimestamp(int(now.timestamp()),tz=timezone.utc))


print("===============================时间加减（timedelta）=============================================")
#  时间加减（timedelta）
print(now + timedelta(days=1))        # 明天
print(now - timedelta(hours=3))       # 3 小时前
print(now + timedelta(weeks=2))       # 两周后
print(now + timedelta(days=1, hours=2, minutes=30))
d1 = datetime(2026, 10, 21)
d2 = datetime(2026, 12, 25)
delta = d2 - d1
print(delta.days)               # 65
print(delta.total_seconds())    # 总秒数


print("=================================calendar学习===========================================")
import calendar


print(calendar.isleap(2024))        # True 闰年判断
print(calendar.month(2026, 10))     # 打印月历字符串
print(calendar.weekday(2026, 10, 21))  # 星期几(0=周一)
calendar.prmonth(2026, 10)          # 直接打印月历


print("=================================datetime学习===========================================")
print(datetime.min.time())
print(datetime.max.time().replace(microsecond=0))

def get_today_range():
    """获取今天 00:00:00 和 23:59:59"""
    today = datetime.now().date()
    start = datetime.combine(today, datetime.min.time())
    end = datetime.combine(today, datetime.max.time())
    return start, end

def get_week_range():
    """本周一 到 本周日"""
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday

def get_month_range():
    """本月第一天 到 本月最后一天"""
    today = datetime.now()
    first_day = today.replace(day=1)
    # 下个月第一天减一天
    next_month = (first_day + timedelta(days=32)).replace(day=1)
    last_day = next_month - timedelta(days=1)
    return first_day, last_day


print(get_today_range())
print(get_week_range())
print(get_month_range())
