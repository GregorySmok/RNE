data = 49**6 + 7**18-21
rebuild = ''
while data != 0:
    rebuild += str(data % 7)
    data //= 7
print(rebuild.count('6'))
