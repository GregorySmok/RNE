minans = []
for n in range(1000, 10000):
    s1 = int(str(n)[0]) + int(str(n)[1])
    s2 = int(str(n)[2]) + int(str(n)[3])
    ans = int(''.join(list(map(str, sorted([s1, s2], reverse=True)))))
    if ans == 1311:
        minans.append(n)
print(min(minans))
    