for a in range(1000, 0, -1):
    k = 0
    for x in range(200):
        for y in range(200):
            if (7*y + 5*x < 1000) or (x < y) or (a < x):
                k += 1
    if k == 40000:
        print(a)
