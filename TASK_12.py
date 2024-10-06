d = '1' + '8' * 80
while '18' in d or '288' in d or '3888' in d:
    if '18' in d:
        d = d.replace('18', '2', 1)
    elif '288' in d:
        d = d.replace('288', '3', 1)
    else:
        d = d.replace('3888', '1', 1)
print(d)
