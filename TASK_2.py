for n in (0, 1):
    for k in (0, 1):
        for m in (0, 1):
            for l in (0, 1):
                if not (not n or k and not m or (l == m)):
                    print(m, l, k, n)
