def g(f, s, h, pob):
    if f + s >= 189:
        return h in pob
    if h > max(pob):
        return 0
    m = [g(f + s, s, h + 1, pob), g(f, s + f, h + 1, pob)]
    if f > s:
        m.append(g(f, f, h + 1, pob))
    if f < s:
        m.append(g(s, s, h + 1, pob))
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for x in range(1, 184):
    if g(5, x, 0, [2]) != 1 and g(5, x, 0, [2, 4]) == 1:
        print(x)
