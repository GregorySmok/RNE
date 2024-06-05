for n in range(50):
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '0'
        n2 = '10' + n2[2:]
    else:
        n2 += '1'
        n2 = '11' + n2[2:]
    if int(n2, 2) >= 16:
        print(n)
