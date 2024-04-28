for n in range(1, 10000):
    n2 = bin(n)[2:-1]
    if n % 2 == 0:
        n2 += '01'
    else:
        n2 += '10'
    if int(n2, 2) == 2017:
        print(n)