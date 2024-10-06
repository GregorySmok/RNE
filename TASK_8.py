from itertools import product
import time

count = 0
for el in product('абвгд', repeat=5):
    string = ''.join(el)
    if string[0] != 'а':
        if 'аа' not in string and 'бб' not in string and 'вв' not in string and 'гг' not in string and 'дд' not in string:
            count += 1
print(count)
