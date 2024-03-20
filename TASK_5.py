for n in range(100000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '0' * n2.count('0')
    else:
        n2 = '1' * n2.count('1') + n2
    if int(n2, 2) > 2000:
        print(n)
        break
