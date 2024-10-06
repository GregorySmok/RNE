def g(f, h, pob):
    if f >= 68:
        return h in pob
    if h > max(pob):
        return 0
    m = [g(f + 1, h + 1, pob), g(f + 4, h + 1, pob), g(f * 5, h + 1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for s in range(1, 68):
    if g(s, 0, [2]) == 0 and g(s, 0, [2, 4]):
        print(s)
