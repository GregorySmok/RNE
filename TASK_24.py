with open('DATA/1_24.txt') as file:
    data = file.readline().replace('TT', '*')
count_TT = 0
unstr = ''
minlen = 10000000000000
for el in data:
    if count_TT == 150:
        minlen = min(minlen, len(unstr))
        unstr = ''
        count_TT = 0
    if el == '*':
        unstr += 'TT'
        count_TT += 1
    else:
        unstr += el
print(minlen)

    
