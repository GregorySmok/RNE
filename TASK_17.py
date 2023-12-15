with open('DATA/17 (2).txt') as file:
    data = [int(i) for i in file]
min3 = 1000
for el in data:
    if 100 <= el < 1000:
        if el % 10 == 3 and el < min3:
            min3 = el
count = 0
qs = 0
for i in range(len(data) - 1):
    if (len(str(data[i])) == 4) !=  (len(str(data[i+1])) == 4):
        if sum([data[i]**2, data[i+1]**2]) % min3 == 0:
            count += 1
            if sum([data[i]**2, data[i+1]**2]) > qs:
                qs = sum([data[i]**2, data[i+1]**2])
print(count, qs)
