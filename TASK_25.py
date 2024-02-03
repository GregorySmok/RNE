for i in range[1]:
    dels = []
    for dl in range(2, round(i**0.5) + 1):
        if len(set(dels)) > 3:
            break
        if i % dl == 0:
            dels.append(dl)
            dels.append(i // dl)
    if len(set(dels)) == 3:
        print(i, max(dels))
