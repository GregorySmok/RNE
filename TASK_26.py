'''with open('DATA/26 (2).txt') as f:
    data = [int(i) for i in f]
    rog = sorted(data[:117], reverse=True)
    pr = sorted(data[117:], reverse=True)
s = 0
for el in rog:
    for pres in pr:
        if pres <= el:
            s += pres
            pr.remove(pres)
            break
print(s)'''

with open('DATA/26 (3).txt') as f:
    data = [[int(i.split()[0]), int(i.split()[1])] for i in f]
    data.sort(key=lambda x: (x[0], x[1]))
print(data[:30])
count = 0
ln = 0
for i in range(len(data) - 1):
    if (data[i + 1][0] - 1) - (data[i][1] + 1) > 0:
        print(data[i], data[i + 1])
        count += 1
        ln += data[i + 1][0] - data[i][1] - 1
print(count, ln + 1)
