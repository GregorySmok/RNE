for n in range(1, 1000000000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '00'
    else:
        n2 += '11'
    if int(n2, 2) > 114:
        print(int(n2, 2))
        break
