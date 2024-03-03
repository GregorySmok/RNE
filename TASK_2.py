for a in (0, 1):
    for b in (0, 1):  # (a→b)∧(b→c)∧(c→d)
        for c in (0, 1):
            for d in (0, 1):
                if (a <= b) and (b <= c) and (c <= d):
                    print(a, d, c, b)
