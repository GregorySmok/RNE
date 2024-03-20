with open('DATA/26 (5).txt') as f:
    data = [list(map(int, i.split())) for i in f]
stat = {}
for el in data:
    stat[el[0]] = stat.get(el[0], []) + [el[2]]
count = 0
sm = 0
for key in stat.keys():
    if len(stat[key]) >= 2:
        count += 1
        sm += sorted(stat[key], reverse=True)[1]
print(count, sm)
