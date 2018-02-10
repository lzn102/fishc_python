# -*- coding: utf-8 -*-

#打印乘法口诀表

for x in range(1,10):
    for y in range(1,x):
        print("%dx%d=%d"%(x,y,x*y), end=' ')
    print("%dx%d=%d"%(x,x,x*x))



