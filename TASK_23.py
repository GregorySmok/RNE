def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    s = 0
    for el in str(start):
        s += int(el)
    return f(start - s, end) + f(start - int(str(start**2)[0]), end)


print(f(32, 1))
