m = 0
for n in range(4, 10000):
    data = '3' + '5' * n
    while '333' in data or '555' in data:
        if '555' in data:
            data = data.replace('555', '3', 1)
        else:
             data = data.replace('333', '5', 1)
    s = sum([int(i) for i in data])
    if s > m:
        m = s
print(m)
