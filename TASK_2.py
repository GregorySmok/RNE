print('x z y w')
for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):
                if (((w <= (not(x))) == (z <= y)) and (y or w)):
                    print(x, w, y, z)
