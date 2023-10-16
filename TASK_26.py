with open('27888.txt') as file:
    data = [i for i in file]
info = data[0].rstrip('\n').split()
data = sorted([int(i) for i in data[1:]])
files = []
for i in range(len(data) - 1):
    files.append(data[i])
    if sum(files) + data[i+1] > int(info[0]):
        break
print(len(files), max(files), sum(files))
