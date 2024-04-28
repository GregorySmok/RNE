from itertools import product

count = 0
for el in product('ГОД', repeat=6):
    if el[0] in 'ГД' and el[-1] in 'ГД':
        count += 1
print(count)