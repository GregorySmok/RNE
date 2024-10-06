for a in range(1000):
    k = 0
    for x in range(300):
        for y in range(300):
            if (2*x + 3*y < 30) or (x + y >= a):
                k += 1
    if k == 90000:
        print(a)
