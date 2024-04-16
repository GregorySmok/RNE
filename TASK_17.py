with open('DATA/17 (8).txt') as f:
    data = [int(i) for i in f]
    m21 = max(filter(lambda x: x % 21 == 0, data))
count = 0
ms = 1111111111110
for i in range(len(data) - 1):
    if (data[i] > m21) + (data[i + 1] > m21) >= 1:
        count += 1
        ms = min(ms, data[i] + data[i + 1])
print(count, ms)
