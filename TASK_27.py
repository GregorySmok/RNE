with open('DATA/27990_B.txt') as file:
    data = [int(i) for i in file]
count = 0
for i in range(1, len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] * data[j]) % 62 == 0:
            count += 1
print(count)
