with open('DATA/24 (2).txt') as f:
    d = f.readline().split('AHAHA')
print(len(max(d, key=len)) + 8)
