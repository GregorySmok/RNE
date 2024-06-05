with open('DATA/17_r.txt') as f:
    d = [int(i) for i in f]
count = 0
ms = 0
for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        if abs(d[i] - d[j]) % 2 == 0:
            if (d[i] % 19 == 0) or (d[j] % 19 == 0):
                count += 1
                ms = max(ms, d[i] + d[j])
print(count, ms)
