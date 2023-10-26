for a in range(10000):
    k = 0
    for x in range(500):
        if (x & 49 == 0) <= ((x & 28 != 0) <= (x & a != 0)):
            k += 1
    if k == 500:
        print(a)
        break
print('not found')
