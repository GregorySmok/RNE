with open('DATA/24 (4).txt') as f:
    data = f.readline().split('AB')
print(len(max(data, key=len)) + 2)
