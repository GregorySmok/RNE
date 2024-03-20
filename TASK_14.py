for n in range(200, 0, -1):
    n4 = ''
    k = n
    while k != 0:
        n4 += str(k % 4)
        k //= 4
    if n4[::-1][-3:] == '123':
        print(n, n4[::-1])
