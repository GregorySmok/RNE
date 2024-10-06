with open('DATA/17 (6).txt') as f:
    d = [int(i) for i in f]
count = 0
ms = 0
for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        f = d[i]
        s = d[j]
        if (f + s) % 2 != 0:
            if f * s % 3 == 0:
                count += 1
                ms = max(ms, f + s)
print(count, ms)
