def func(f, s, h, pob):
    if f+s >= 151:
        return h in pob
    if h > max(pob):
        return 0
    m = [func(f, s+1, h+1, pob), func(f+1, s, h+1, pob), func(f, s*4, h+1, pob), func(f*4, s, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return any(m)
    
for s in range(1, 142):
    if func(9, s, 0, [2]) == 1:
        print(s)
