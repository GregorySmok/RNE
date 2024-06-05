count = 0
for one in '0':
    for two in '01':
        for three in '01':
            for four in '01':
                for five in '01':
                    for six in '01':
                        for seven in '01':
                            for eight in '01':
                                ip = one + two + three + four + five + six + seven + eight
                                if ip != '00000000':
                                    if ip == ip[::-1]:
                                        count += 1
print(count)
