data = '7' * 47
while '2222' in data or '7777' in data:
    if '2222' in data:
        data = data.replace('2222', '77', 1)
    else:
        data = data.replace('7777', '22', 1)
print(data)
