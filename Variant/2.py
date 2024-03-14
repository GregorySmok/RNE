for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):  # (x ≡ (y → z)) ∧ (¬w → (x ≡ y))
            for w in (0, 1):
                if (x == (y <= z)) and ((not w) <= (x == y)):
                    print(y, w, z, x)
