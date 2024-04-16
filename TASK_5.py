for n in range(100000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '1' + n2 + '1'
    else:
        n2 += '10'
    if int(n2, 2) > 179:
        print(n)
        break
