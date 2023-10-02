for n in range(100, 1000):
    f = n//100 * n%100//10
    s = int(str(n)[1]) * int(str(n)[2])
    a = sorted([f, s], reverse=True)
    res = str(a[0]) + str(a[1])
    if res == '123':
        print(n)
        break