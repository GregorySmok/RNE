alf = '0123456789ABCDE'
data = 3 * 15**1140 + 2 * 15**1025 + 15**923 - 3 * 15**85 + 2 * 15**74 + 3
d = ''
while data != 0:
    d += alf[data % 15]
    data //= 15
print(d.count('E'))
