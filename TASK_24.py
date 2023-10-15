f = open('24.txt')
data = f.readline()
shelf = {}
for i in range(len(data) - 1):
    if data[i] == 'E':
        if data[i+1] not in shelf.keys():
            shelf[data[i+1]] = 0
        shelf[data[i+1]] += 1
mass = []
for key in shelf.keys():
    mass.append([key, shelf[key]])
mass = sorted(mass, key=lambda x: x[1])
print(mass[-1][0])