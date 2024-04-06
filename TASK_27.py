with open('DATA/27B.txt') as file:
    data = [int(i) for i in file]
pre3 = 0
pre7 = 0
pre21 = 0
pre = 0
mpr = 0
for i in range(len(data)):
    if data[i] % 21 == 0:
        if pre != 0:
            mpr = max(data[i] * pre, mpr)
        pre21 = max(data[i], pre21)
    elif data[i] % 3 == 0:
        if pre7 != 0:
            mpr = max(mpr, data[i] * pre7)
        pre3 = max(pre3, data[i])
    elif data[i] % 7 == 0:
        if pre3 != 0:
            mpr = max(mpr, data[i] * pre3)
        pre7 = max(pre7, data[i])
    else:
        if pre21 != 0:
            mpr = max(mpr, data[i] * pre21)
    pre = max(pre, data[i])
print(mpr)
