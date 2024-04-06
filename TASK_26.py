with open('DATA/26 (6).txt') as f:
    time = int(f.readline())
    data = sorted([int(i) for i in f])

tasks = []
for el in data:
    if sum(tasks) + el <= time:
        tasks.append(el)
print(len(tasks))
