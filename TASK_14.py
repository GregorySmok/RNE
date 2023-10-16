data = 9**8*3**20-3**10-3
rebuild = ''
while data != 0:
    rebuild += str(data % 3)
    data //= 3
print(rebuild.count('2'))
