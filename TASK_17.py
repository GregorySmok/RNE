with open('DATA/117.txt') as file:
    data = [int(i) for i in file]
count = 0
sm = 0
for i in range(len(data) - 2):
    if data[i]**2 + data[i+1]**2 == data[i+2]**2 or data[i+1]**2 + data[i+2]**2 == data[i]**2 or data[i]**2 + data[i+2]**2 == data[i+1]**2:
        count += 1
        if data[i] + data[i+1] + data[i+2] > sm:
            sm = data[i] + data[i+1] + data[i+2]
print(count, sm)
