data = '1'*39 + '2'*39
while '111' in data:
    data = data.replace('111', '2', 1)
    data = data.replace('222', '1', 1)
print(data)
