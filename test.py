count = 0
for n in range(1000, 10000):
    if str(n)[0] in '24680':
        r = int(str(n)[0]) + int(str(n)[2]) + \
            abs(int(str(n)[1]) - int(str(n)[3]))
    else:
        d = int(''.join(sorted(str(n))))
        r = bin(d)[2:].count('1')
    if r > 20:
        count += 1
print(count)
