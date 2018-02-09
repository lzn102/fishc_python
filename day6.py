# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 打印斐波那契数列

def fln(n):
    put = [0, 1]

    for x in range(n):
        put0 = put[-1]
        put1 = put[-2] + put[-1]
        put[-1] = put0
        put.append(put1)

    print(put)

h = int(input("number:\n"))
fln(h)








