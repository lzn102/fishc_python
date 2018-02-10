# -*- coding: utf-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出

a = int(input("input a number:"))
b = int(input("input again:"))
c = int(input("input again again:"))


if a <= b <= c:
    min_ = a
    middle = b
    max_ = c
    print("min to max is: %d" % min_, middle, max_)
elif a <= c <= b:
    min_ = a
    middle = c
    max_ = b
    print("min to max is: %d" % min_, middle, max_)
elif b <= a <= c:
    min_ = b
    middle = a
    max_ = c
    print("min to max is: %d" % min_, middle, max_)
elif b <= c <= a:
    min_ = b
    middle = c
    max_ = a
    print("min to max is: %d" % min_, middle, max_)
elif c <= a <= b:
    min_ = c
    middle = a
    max_ = b
    print("min to max is: %d" % min_, middle, max_)
elif c <= b <= a:
    min_ = c
    middle = b
    max_ = a
    print("min to max is: %d" % min_, middle, max_)

