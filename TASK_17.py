with open('DATA/1777.txt') as file:
    data = [int(i) for i in file]
m29 = max(data, key=lambda x: str(x)[-2::] == '29')
ms = 0
count = 0
for i in range(len(data) - 2):
    is_l5 = [len(str(abs(data[i]))) == 5, len(str(abs(data[i + 1]))) == 5, len(str(abs(data[i + 2]))) == 5]
    if sum(is_l5) == 2 and sum([data[i], data[i + 1], data[i + 2]]) <= m29:
        count += 1
        if sum([data[i], data[i + 1], data[i + 2]])> ms:
            ms = sum([data[i], data[i + 1], data[i + 2]])
print(count, ms)

