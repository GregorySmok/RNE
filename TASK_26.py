with open('DATA/27881.txt') as file:
    data = [i for i in file]
info = data[0].rstrip('\n').split()
data = sorted([int(i) for i in data[1:]])
files = []
for i in range(len(data)):
    if data[i] + sum(files) <= int(info[0]):
        files.append(data[i])
print(len(files))
print(files)
print(sum(files))
