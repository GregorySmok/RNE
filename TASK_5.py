for n in range(10000):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 = '11' + n2
    else:
        n2 += '00'
    if int(n2, 2) > 116:
        print(n)
        break
