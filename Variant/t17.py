with open("trex.txt") as f:
    data = [int(i) for i in f]
count = 0
ms = 0
for i in range(len(data) - 1):
    for j in range(i + 1 < len(data)):
        if (data[i] + data[j]) % 60 == 0 and (data[i] % 40 == 0 or data[j] % 40 == 0):
            count += 1
            ms = max(ms, data[i] + data[j])
print(count)
print(ms)
