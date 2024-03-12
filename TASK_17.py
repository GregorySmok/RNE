with open('DATA/17 (3).txt') as file:
    data = [int(i) for i in file]
min3 = sorted([i for i in data if 100 <= i < 1000])[1]
print(min3)
count = 0
ms = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] < min3**2:
        count += 1
        ms = max(ms, data[i] + data[i + 1])
print(count, ms)
