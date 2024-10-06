ans = set()
for n in range(100, 3001):
    n2 = bin(n)[3:]
    if len(n2) == 0:
        n2 = '0'
    while len(n2) > 1 and n2[0] == '0':
        n2 = n2[1:]
    ans.add(n - int(n2, 2))
print(len(ans))
