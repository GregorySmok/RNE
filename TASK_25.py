for n in range(45000000, 50000001):
    dels = []
    for dl in range(1, round(n**0.5 / 2) + 1):
        if n % dl == 0:
            if dl % 2 != 0:
                dels.append(dl)
            if n // dl % 2 != 0:
                dels.append(n // dl)
        if len(dels) > 5:
            break
    if len(dels) == 5:
        print(n)
