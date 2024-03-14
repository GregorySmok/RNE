with open('DATA/263.txt') as f:
    data = sorted([int(i) for i in f])
v = 7291
can = []
for i in range(len(data)):
    if sum(can) + data[i] <= v:
        can.append(data[i])
    else:
        break
for i in range(len(data)):
    if sum(can) - can[-1] + data[i] <= 7291:
        can[-1] = data[i]
print(len(can), max(can), sum(can))
