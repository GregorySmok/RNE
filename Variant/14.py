data = 36**7 + 6**19 - 18
hex = ''
while data != 0:
    hex += str(data % 6)
    data //= 6
print(hex.count('0'))
