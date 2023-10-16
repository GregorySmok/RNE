count = 0
for i1 in 'абрикос':
    for i2 in 'абрикос':
        for i3 in 'абрикос':
            for i4 in 'абрикос':
                for i5 in 'абрикос':
                    for i6 in 'абрикос':
                        for i7 in 'абрикос':
                            s = i1+i2+i3+i4+i5+i6+i7
                            if s.count(s[0]) == 1 and s.count(s[1]) == 1 and s.count(s[2]) == 1 and s.count(s[3]) == 1 and s.count(s[4]) == 1 and s.count(s[5]) == 1 and s.count(s[6]) == 1:
                                ok = True
                                for el in ['аи', 'иа','ао','оа','ио','ои','бр','рб','бк','кб','бс','сб','рк','кр','рс','ср','кс','ск']:
                                    if el in s:
                                        ok = False
                                        break
                                if ok:
                                    count +=1
print(count)