with open('DATA/26.txt') as f:
    q = []
    z = []
    for el in f:
        if el.split()[1] == 'Q':
            q.append(int(el.split()[0]))
        else:
            z.append(int(el.split()[0]))
    q.sort()
    z.sort()
budget = 110
lost = 0
bought_z = 0
for el in z:
    if el <= budget - lost:
        lost += el
        bought_z += 1
for el in q:
    if el <= budget - lost:
        lost += el
print(bought_z, budget - lost)
