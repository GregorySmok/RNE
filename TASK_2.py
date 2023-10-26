print('z w x y')
for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):
                if ((not (w) or (y == z)) and (y == (not (z) or x))):
                    print(z, w, y, x)
