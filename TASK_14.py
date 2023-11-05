for x in list(range(10)) + ['a']:
    for y in list(range(10)) + ['a']:
        s = int('7' + str(y) + '23' + str(x) + '5', 25) + \
            int('67' + str(x) + '9' + str(y), 11)
        if s % 131 == 0:
            print(s / 131)
