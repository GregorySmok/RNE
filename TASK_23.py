def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return f(start + 1, end) + f(start * 2, end)


print(f(3, 6) * f(6, 12) * f(12, 16))
