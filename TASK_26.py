with open('DATA/107_26.txt') as f:
    d = sorted([tuple([int(r)for r in i.split()]) for i in f], reverse=True)
for i in range(len(d) - 1):
    if d[i][0] == d[i + 1][0]:
        if d[i][1] - 14 == d[i + 1][1]:
            print(d[i + 1], d[i])
