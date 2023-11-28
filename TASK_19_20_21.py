def f(s, h, pob, n):
    global last
    if s >=50:
        return h in pob
    if h > max(pob) or n == last:
        return 0
    last = n
    m = [f(s+1, h+1, pob, 1), f(s+2, h+1, pob, 2), f(s*2, h+1, pob, 3)]
    if h % 2 != max(pob) % 2:
        return any(m)
    else:
        return all(m)

last = 10000
for s in range(1, 50):
    if f(s, 0, [1], 0) != 1 and f(s, 0, [2], 0) == 1:
        print(s)