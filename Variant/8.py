from itertools import permutations

count = 0
for el in permutations('демьян', 6):
    st = ''.join(el)
    if st[0] != 'ь' and 'еь'not in st and 'яь'not in st:
        count += 1
print(count)
