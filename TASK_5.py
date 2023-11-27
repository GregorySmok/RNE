for n in range(1, 1000000000):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', 'q').replace('1', '0').replace('q', '1')
    while len(n2) > 1 and n2[0] != '1':
        n2 = n2[1::]
    if n - int(n2, 2) == 979: 
        print(n)
        break