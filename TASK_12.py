data = '7' * 200
while '7777' in data or '333333' in data:
    if '333333' in data:
        data = data.replace('33333', '777', 1)
    else:
        data = data.replace('777', '33', 1)
print(data.count('3'))
