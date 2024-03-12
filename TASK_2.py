for a in (0, 1):
    for b in (0, 1):  # b≡a∨c→b
        for c in (0, 1):
            if b == a or c <= b:
                print(c, a, b)
print()
for a in (0, 1):
    for b in (0, 1):  # b≡(a∨(c→b))
        for c in (0, 1):
            if b == (a or (c <= b)):
                print(c, a, b)
