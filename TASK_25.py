for el in range(125256, 125331):
    dels = []
    for dl in range(2, el + 1):
        if el % dl == 0 and dl % 2 == 0:
            dels.append(dl)
    if len(dels) == 6:
        print(dels)
