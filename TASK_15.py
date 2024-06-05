for a in range(1000, 0, -1):
    k = 0
    for x in range(300):
        for y in range(300):  # ((x≥A)∨(121≥x2))∧((y2<49)∨(A < y))
            if ((x >= a) or (121 >= x ** 2)) and ((y**2 < 49) or (a < y)):
                k += 1
    if k == 90000:
        print(a)
        break
