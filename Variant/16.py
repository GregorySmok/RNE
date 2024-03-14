count = 0
for i in range(100000000, 1000000000):
    if bin(i)[2:].count('1') == 2:
        count += 1
print(count)
