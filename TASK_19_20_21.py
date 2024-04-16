def g(f, s, h, pob):
    if f + s >= 143:
        return h in pob
    if h > max(pob):
        return 0
    var = [g(f + 3, s, h + 1, pob), g(f * 2, s, h + 1, pob),
           g(f, s + 3, h + 1, pob), g(f, s * 2, h + 1, pob)]
    if h % 2 != max(pob) % 2:
        return any(var)
    else:
        return all(var)


for k in range(1, 124):
    if g(16, k, 0, [2, 4]) == 1 and g(16, k, 0, [2]) != 1:
        print(k)
