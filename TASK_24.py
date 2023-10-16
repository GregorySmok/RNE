f = open('24_demo.txt')
data = f.readline()
mx = 0
ln = 0
for i in range(len(data)):
    if data[i] == 'Z':
        ln += 1
        ind = i + 1
        try:
            nxt = data[ind]
            while nxt == 'Z':
                ln += 1
                ind += 1
                nxt = data[ind]
        except:
            pass
        if ln > mx:
            mx = ln
        ln = 0
print(mx)
