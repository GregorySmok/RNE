for n in range(100, 1000):
    f = int(str(n)[0]) * int(str(n)[1])
    s = int(str(n)[1]) * int(str(n)[2])
    ans = ''.join(sorted([str(f), str(s)], key=int))
    if ans == '621':
        print(n)
