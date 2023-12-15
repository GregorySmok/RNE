for a in range(1000):
    k = 0
    for x in range(300):
        if ((x&28 != 0) or (x&45 != 0)) <= ((x&17 == 0) <= (x&a != 0)):
            k += 1
    if k == 300:
        print(a)
        break