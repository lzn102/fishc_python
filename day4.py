# -*- coding: utf-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天？

year = int(input("now_year:"))
month = int(input("now_month:"))
day = int(input("now_day:"))
p = "today is %d days in now year"

if year % 4 != 0:
    two_month = 28
else:
    two_month = 29


if month == 1:
    days = day
    print( p %days)
elif month == 2:
    days = 31 + day
    print( p %days)
elif month == 3:
    days = 31 + two_month + day
    print(p %days)
elif month == 4:
    days = 31 + two_month + 31 + day
    print(p %days)
elif month == 5:
    days = 31 + two_month + 31 + 30 + day
    print(p %days)
elif month == 6:
    days = 31 + two_month + 31 + 30 + 31 + day
    print(p %days)
elif month == 7:
    days = 31 + two_month + 31 + 30 + 31 + 30 + day
    print=(p %days)
elif month == 8:
    days = 31 + two_month + 31 + 30 + 31 + 30 + 31 + day
    print(p %days)
elif month == 9:
    days = 31 + two_month + 31 + 30 + 31 + 30 + 31 + 31 + day
    print(p %days)
elif month == 10:
    days = 31 + two_month + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
    print(p %days)
elif month == 11:
    days = 31 + two_month + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
    print(p %days)
elif month == 12:
    days = 31 + two_month + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
    print(p %days)


