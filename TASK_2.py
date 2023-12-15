print("z y x")
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            if not((x or y) <= (z == x)):
                print(x, z, y)
