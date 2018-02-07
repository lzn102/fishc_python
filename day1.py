# 四个数字1234能组成多少个互不相同且无重复的三位数数字


number = []

for x in range(1, 5):
    x = x * 100

    for y in range(1, 5):
        y = y * 10

        for z in range(1, 5):
            number_sum = x + y + z
            number.append(number_sum)


number_ch = []

for x in number:
    x = str(x)

    if x[0] == x[1] or x[0] == x[2] or x[1] ==x[2]:
        pass
    else:
        x = int(x)
        number_ch.append(x)


print("1234能组成的没有重复数字的三位数有%d个" %len(number_ch))

