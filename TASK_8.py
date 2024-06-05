from itertools import product

count = 0
for el in product('воздух', repeat=5):
    string = ''.join(el)
    if string.count('о') == 1 and string.count('у') == 1:
        new = ''
        for l in string:
            if l in 'вх':
                new += '*'
            else:
                new += l
        if '*о' not in string and 'о*' not in string and '*у' not in string and 'у*' not in string:
            count += 1
print(count)
