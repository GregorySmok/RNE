def g(f, s, h, pob):
    if f + s >= 150:
        return h in pob
    if h > max(pob):
        return 0
    m = [g(f + 2, s, h + 1, pob), g(f, s + 2, h + 1, pob),
         g(f * 3, s, h + 1, pob), g(f, s * 3, h + 1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for s in range(1, 134):
    if g(16, s, 0, [2, 4]) == 1 and g(16, s, 0, [2]) != 1:
        print(s)
