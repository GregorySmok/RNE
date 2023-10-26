def func(f, s, h, pob):
    if f + s >= 84:
        return h in pob
    if h > max(pob):
        return 0
    m = [func(f+1, s, h+1, pob), func(f, s+1, h+1, pob),
         func(f*2, s, h+1, pob), func(f, s*3, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for s in range(1, 68):
    if func(16, s, 0, [4]) == 1 and func(16, s, 0, [2]) != 1:
        print(s)
