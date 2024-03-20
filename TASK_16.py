import sys
sys.setrecursionlimit(10**7)


def f(n):
    if n >= 2024:
        return 1
    return f(n + 2) + f(n + 4)


m = []
for k in range(30):
    m.append(f(k))
print(m)
