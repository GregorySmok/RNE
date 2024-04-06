def g(f, h, pob):
    if f >= 200:
        return h in pob
    if h > max(pob):
        return 0
    m = [g(f + 1, h + 1, pob), g(f * 3, h + 1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for k in range(1, 200):
    if g(k, 0, [2]) != 1 and g(k, 0, [2, 4]) == 1:
        print(k)
