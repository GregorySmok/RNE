def sum_of_nums(num):
    s = 0
    for el in str(abs(num)):
        s += int(el)
    return s


with open("DATA/17 (5).txt") as f:
    data = [int(i) for i in f]
count = 0
ms = 0
m3 = max(data, key=lambda x: len(str(x)) == 3)
for i in range(len(data) - 1):
    if (sum_of_nums(data[i]) % 5 == 0 and sum_of_nums(data[i + 1]) % 5 != 0) or (sum_of_nums(data[i]) % 5 != 0 and sum_of_nums(data[i + 1]) % 5 == 0):
        if abs(data[i]**2 - data[i + 1]**2) >= m3**3:
            count += 1
            ms = max(ms, data[i] + data[i + 1])
print(count, ms)
