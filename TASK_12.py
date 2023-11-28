data = '3' * 68
while '999' in data or '333' in data:
    if '333' in data:
        data = data.replace('333', '9', 1)
    else:
        data = data.replace('999', '3', 1)
print(data)
