print('z w x y')
for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):
                if not (not (not (z) == y) or ((w and not x) == (y and x))):
                    print(z, w, x, y)
