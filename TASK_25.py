def dels(n):
    dls = []
    for i in range(1, round(n**0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                dls.append(i)
            if n // i % 2 != 0:
                dls.append(n // i)
        if len(dls) > 5:
            return False
    if len(dls) == 5:
        return True


for num in range(35000000, 40000001):
    if dels(num):
        print(num)
