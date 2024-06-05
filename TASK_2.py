for x in (0, 1):
    for y in (0, 1):
        for w in (0, 1):
            for u in (0, 1):
                if (not ((y <= w) == x)) and u:
                    print(u, x, w, y)
