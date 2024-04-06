def dl(f, b):
    return f % b == 0


for a in range(1, 1000):
    k = 0
    for x in range(1, 101):
        if (dl(x, 30) and (not dl(x, 45))) <= (not dl(x, a)):
            k += 1
    if k == 100:
        print(a)
        break
