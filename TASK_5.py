for n in range(1, 1000000000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '10'
    else:
        n2 += '01'
    if int(n2, 2) <= 102:
        print(int(n2, 2))
    else:
        break
