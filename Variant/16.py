def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    if n % 2 == 0 and n > 0:
        return f(n // 2)


count = 0
for a in range(100000000):
    k = a
    if f(k) == 2:
        count += 1
print(count)
