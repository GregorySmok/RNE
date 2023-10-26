from itertools import product

count = 0
num = 0
for el in product(sorted('алгоритм'), repeat=5):
    num += 1
    if num % 2 != 0 and el[0] != 'г' and el.count("и") >= 2:
        count += 1
print(count)
