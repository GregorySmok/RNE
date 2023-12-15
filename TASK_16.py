count = 0
for n in range(765432015, 1542613240):
    first = sum([int(i) for i in str(n)])
    second = sum([int(i) for i in str(n+1)])
    if first > second:
        count += 1
print(count)