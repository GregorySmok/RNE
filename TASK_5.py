for n in range(10, 100):
    nn = str(n // 10 + n % 10)
    if len(nn) == 2:
        print(n)
        break
