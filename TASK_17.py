with open('DATA/17 (7).txt') as f:
    data = [int(i) for i in f]
    m3 = max(filter(lambda x: len(str(x)) == 3, data))
count = 0
ms = 0
for i in range(len(data) - 1):
    if (len(str(data[i])) == 3) + (len(str(data[i + 1])) == 3) == 1 and data[i] + data[i + 1] >= m3:
        count += 1
        ms = max(ms, data[i] + data[i + 1])
print(count, ms)
