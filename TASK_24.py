f = open('DATA/24.txt')
data = f.readline()
mx = 0
ln = ''
for i in range(len(data)):
    if data[i] != 'E':
        ln += data[i]
    else:
        if ln.count('A') >= 3:
            if len(ln) > mx:
                mx = len(ln)
        ln = ''
print(mx)
