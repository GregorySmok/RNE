import sys
sys.setrecursionlimit(10**6)


def f(n):
    if n == 1:
        return 1
    return n * f(n-1) - 1


print(f(1000)/f(997))
