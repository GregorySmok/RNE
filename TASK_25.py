count = 0
norm = 123456
while count != 5:
    norm += 1
    dels = []
    for dl in range(2, round(norm**0.5) + 1):
        if norm % dl == 0:
            if dl**2 == norm:
                dels.append(dl)
            else:
                dels.append(dl)
                dels.append(norm // dl)
        if len(dels) > 4:
            break
    if len(dels) == 4:
        print(norm, sum(dels), dels)
        count += 1
