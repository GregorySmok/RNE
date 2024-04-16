import sys
sys.setrecursionlimit(50000)


def f(n):
    if n == 2000:
        return 1996947
    if n <= 12:
        return 1
    else:
        return f(n - 1) + n - 2


print(f(2024) - f(2020))
