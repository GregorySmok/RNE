for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):  # ((1≡w)≡(¬((w∧x)∨y)))→z
                if (((1 == w) == (not ((w and x) or y))) <= z):
                    print(x, z, y, w)
