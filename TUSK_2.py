print('w x y z')
for x in (0,1):
    for y in (0, 1):
        for w in (0, 1):
            for z in (0, 1):
                if (not(x) or not(y)) and (x != z) and w:
                    print(w, x, y, z)