with open('DATA/24 (5).txt') as f:
    data = f.readline()
for el in 'AEOU':
    data = data.replace(el, '+')
for el in 'KLMN':
    data = data.replace(el, '-')
data = data.replace('++', '+ +').replace('--', '- -')
data = data.replace('++', '+ +').replace('--', '- -')
data = data.split()
print(len(max(data, key=len)))
