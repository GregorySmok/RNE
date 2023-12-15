data = '7' * 40 + '9' * 40 + '4' * 50
while '49' in data or '97' in data or '47' in data:
    if '47' in data:
        data = data.replace('47', '74', 1)
    if '97' in data:
        data = data.replace('97', '79', 1)
    if '49' in data:
        data = data.replace('49', '94', 1)
print(data)
