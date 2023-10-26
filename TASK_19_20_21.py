def func(f, s, h, pob):
    if f + s >= 41:
        return h in pob
    if h > max(pob):
        return 0
    m = [func(f+1, s+2, h+1, pob), func(f+2, s+1, h+1, pob),
         func(f*2, s, h+1, pob), func(f, s*2, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for s in range(1, 33):
    if (func(8, s, 0, [2]) == 1 or func(8, s, 0, [4]) == 1):
        print(s)
