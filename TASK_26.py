with open('DATA/26 (1).txt') as f:
    data = [[int(i.split()[0]), int(i.split()[1])] for i in f]
    data.sort(key=lambda x: (x[0], x[1]))
mc = 0
lt = 0
for i in range(len(data) - 1):
    cc = 1
    start = data[i]
    last = data[i]
    for j in range(i + 1, len(data)):
        if last[1] <= data[j][0]:
            last = data[j]
            cc += 1
    if mc <= cc:
        mc = cc
        lt = start[0]
print(mc, lt)
