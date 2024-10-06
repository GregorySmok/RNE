with open('DATA/26 (4).txt') as f:
    n = int(f.readline())
    d = [int(i) for i in f]
count = 0
maver = 0
for i in range(n - 1):
    fr = d[i]
    if fr % 2 == 0:
        continue
    for j in range(i + 1, n):
        sc = d[j]
        if fr % 2 != 0 and sc % 2 != 0:
            if ((fr + sc) // 2) in d:
                count += 1
                maver = max(maver, (fr + sc) // 2)
print(count, maver)
