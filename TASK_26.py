from math import ceil

with open('DATA/26 (7).txt') as f:
    n = int(f.readline())
    stars = [int(i) for i in f]
    stars.sort()
taken = [stars[0]]
for el in stars[1:]:
    if el >= ceil(taken[-1] * 1.1):
        taken.append(el)
print(len(taken), taken[-1])
