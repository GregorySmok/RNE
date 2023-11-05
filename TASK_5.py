for n in range(100000000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2, 2)
    if r < 100:
        print(n, r)
    else:
        break
