with open('DATA/24 (4).txt') as f:
    d = [i for i in f]
    base = min(d, key=lambda x: x.count('N'))
dict_ = {}
for el in base:
    if el in dict_.keys():
        dict_[el] += 1
    else:
        dict_[el] = 0
sor = []
for key, value in dict_.items():
    sor.append((value, key))
sor.sort(reverse=True)
print(sor)
