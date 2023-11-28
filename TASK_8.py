from itertools import product

count = 0
num = 0
for el in product('1234', repeat=5):
    if el.count('1') == 2:
        count += 1
print(count)
