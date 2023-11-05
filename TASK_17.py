with open('DATA/338.txt') as file:
    data = [int(i) for i in file]
count = 0
ms = 0
for i in range(len(data) - 1):
    if data[i] % 117 == min(data) or data[i+1] % 117 == min(data):
        count += 1
        if data[i] + data[i+1] > ms:
            ms = data[i] + data[i+1]
print(count, ms)
