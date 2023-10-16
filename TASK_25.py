def func(n):
    print('start')
    natdels = []
    for i in range(2, n + 1):
        if n % i == 0:
            natdels.append(i)
        if len(natdels) == 5:
            break
    if len(natdels) < 5:
        return 0
    pr = 1
    for el in natdels:
        pr *= el
    return pr


count = 0
for i in range(200000000, 10**1000):
    ans = func(i)
    if 0 < ans < i:
        print(ans)
        count += 1
    if count == 5:
        break
