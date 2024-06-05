from functools import lru_cache


@lru_cache(None)
def g(k):
    if k < 10:
        return k
    return g(k - 2) + 1


def f(n):
    return g(n-1)


for i in range(100):
    g(i)

count = 0
for j in range(1, 100):
    if round(f(j)**0.5)**2 == f(j):
        count += 1
print(count)
