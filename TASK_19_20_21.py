def g(f, h, pob):
    if f >= 48:
        return h in pob
    if h > max(pob):
        return 0
    m = [g(f + 1, h + 1, pob), g(f + 3, h + 1, pob), g(f * 2, h + 1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)
    
for s in range(1, 48):
    if g(s, 0, [2, 4]) == 1 and g(s, 0, [2]) != 1:
        print(s)
