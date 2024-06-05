variants = []
for n in range(4, 10000):
    d = '8' + '5' * n
    while '8858' in d or '555' in d:
        if '8858' in d:
            d = d.replace('8858', '4', 1)
        else:
            d = d.replace('555', '58', 1)
        if '5858' in d:
            d = d.replace('5858', '85', 1)
    s = 0
    for el in d:
        s += int(el)
    if s == 66:
        variants.append(n)
print(max(variants))
