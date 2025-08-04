from functools import lru_cache
import sys
sys.setrecursionlimit(10**5)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return (n - 1) * f(n - 1)


print(2024*2023 + 2 * 2023)
