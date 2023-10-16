with open('DATA/17(1).txt') as file:
    data = [int(i) for i in file]
count = 0
sm = 0
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] + data[j]) % 120 == 0:
            count += 1
            if data[i] + data[j] > sm:
                sm = data[i] + data[j]
print(count, sm)
