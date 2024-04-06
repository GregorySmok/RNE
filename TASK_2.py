for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):  # c∧¬b∨c∧a
            if c and (not b) or c and a:
                print(b, c, a)
