def func(f, s, h, pob):
    if f + s >= 75:
        return h in pob
    if h > max(pob):
        return 0
    m = [func(f, s+1, h+1, pob), func(f+1, s, h+1, pob),
         func(f+s, s, h+1, pob), func(f, s + f, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)


for s in range(1, 47):
    if func(7, s, 0, [2]) != 1 and func(7, s, 0, [2, 4]) == 1:
        print(s)
