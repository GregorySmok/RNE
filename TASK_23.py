def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start + 2, end) + f(start + 4, end)

print(f(1, 8) * f(8, 15))