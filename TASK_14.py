def dl(a ,b):
    return a % b == 0


for a in range(1, 300):
    k = 0
    for x in range(1,201):
        for y in range(1, 201):
            if ((dl(144, x)) <= (not(dl(x, y)))) or (x + y > 100) or (a - x > y):
                k += 1
    if k == 40000:
        print(a)
        break
