with open('DATA/24.txt') as file:
    data = file.readline()
alf = 'ABCDEFGHIJKLMNOP'
count = 0
mc = 0
for el in data:
    if el in alf:
        count += 1
    else:
        mc = max(mc, count)
        count = 0
print(mc)
