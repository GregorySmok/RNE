def dl(a, b):
    return a % b == 0


for a in range(1, 1000):
    k = 0
    for x in range(1, 101):
        if dl(a, 45) and (dl(750, x) <= ((not dl(a, x)) <= (not dl(120, x)))):
            k += 1
    if k == 100:
        print(a)
        break
