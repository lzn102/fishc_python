# 一个整数加上100和加上268后都是一个完全平方数,求该数

import math

for i in range(10000):
    x = math.sqrt(i + 100)
    y = math.sqrt(i + 268)

    # 1余任何整数返回0
    if x % 1 == 0 and y % 1 ==0:
        print(i)