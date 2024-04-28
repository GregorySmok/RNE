for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1): #(x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w
            for w in (0, 1):
                if not((x and not y) or ( x == z) or not w):
                    print(x, w, z, y)
