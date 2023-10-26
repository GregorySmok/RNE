for n in range(100, 0, -1):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += bin(3 * (n % 3))[2:]
    r = int(n2, 2)
    if r < 100:
        print(n)
