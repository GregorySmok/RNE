from itertools import permutations
count = 0
for el in permutations('кабинет', r=7):
    if el[-1] not in ['а', 'и', 'е']:
        count += 1
print(count)
