with open('DATA/17 (9).txt') as f:
    d = [int(i) for i in f]
    mins = min(filter(lambda x: str(x)[-1] == str(x)[-2], d))
count = 0
ms = 0
for i in range(len(d) - 1):
    if (str(d[i])[-1] == str(d[i + 1])[-2]) or (str(d[i + 1])[-1] == str(d[i])[-2]):
        if (abs(d[i]) % 7 == 0) + (abs(d[i + 1]) % 7 == 0) == 1:
            if d[i] ** 2 + d[i + 1]**2 <= mins**2:
                count += 1
                ms = max(ms, d[i] ** 2 + d[i + 1]**2)
print(count, ms)