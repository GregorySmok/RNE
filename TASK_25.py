from fnmatch import fnmatch


for n in range(0, 10**10, 42):
    if fnmatch(str(n), '48*15*0'):
        print(n, n/42)
