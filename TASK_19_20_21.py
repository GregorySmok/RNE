def f(s, h, pob):
    if s >= 94:
        return h in pob
    if h > max(pob):
        return 0
    m = [f(s+1, h+1, pob), f(s*2, h+1, pob)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)
    

for s in range(1, 94):
    if f(s, 0, [2]) != 1 and f(s, 0, [2, 4]) == 1:
        print(s)