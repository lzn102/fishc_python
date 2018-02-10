# -*- coding: utf-8 -*-
# 判断101~200之间的素数

import math

l = []
for x in range(101,201):
    l.append(x)

x = 101
while x in l:
    z = int(math.sqrt(x))
    for y in range(2, z+1):
        s = x % y
        if s == 0:
            try:
                l.remove(x)
            except ValueError:
                pass
    x = x + 1

print(len(l))
print(l)

