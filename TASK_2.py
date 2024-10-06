for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if not ((x == z) or (x <= (y and z))):
                print(z, y, x)
