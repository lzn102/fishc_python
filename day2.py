# -*- coding: utf-8 -*-
# 企业利润计算

sum_money = float(input("输入利润计算应发奖金(单位为万):"))


if 0 < sum_money <= 10:
    money = sum_money * 0.1
    print("应发奖金%f元" %(money * 10000))

elif 10 < sum_money <= 20:
    money = 1 + (sum_money-10) * 0.075
    print("应发奖金%f元" %(money * 10000))

elif 20 < sum_money <= 40:
    money = 1.75 + (sum_money-20) * 0.05
    print("应发奖金%f元" %(money * 10000))

elif 40 < sum_money <= 60:
    money = 2.75 + (sum_money-40) * 0.03
    print("应发奖金%f元" %(money * 10000))

elif 60 < sum_money <= 100:
    money = 3.35 + (sum_money-60) * 0.015
    print("应发奖金%f元" %(money * 10000))

elif sum_money > 100:
    money = 3.95 + (sum_money-100)*0.01
    print("应发奖金%f元" %(money * 10000))
