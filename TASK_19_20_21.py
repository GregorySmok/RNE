def func(s, h, pob):
    if s >= 39:
        return h in pob
    if h > max(pob):
        return 0
    m = [func(s+1, h+1, pob), func(s+2, h+1, pob), func(s*2, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)
    
for s in range(1, 39):
    if func(s, 0, [2]) != 1 and func(s, 0, [2, 4]) == 1:
        print(s)
