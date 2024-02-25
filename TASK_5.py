count = 0
for n in range(100, 1000):
    if str(n).count(str(n)[0]) == 1 and str(n).count(str(n)[1]) == 1 and str(n).count(str(n)[2]) == 1:
        average = sorted([int(i) for i in str(n)])[1]
        num = str(average) + str(n) + str(average)
        while num[0] == '0':
            num = num[1:]
        if int(num) % sum([int(i) for i in num]) == 0:
            count += 1
print(count)
