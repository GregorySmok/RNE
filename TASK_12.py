for n in range(4, 100):
    data = '8' + n * '4'
    while '4444' in data or '844' in data or '84' in data:
        if '4444' in data:
            data = data.replace('4444', '884', 1)
        if '844' in data:
            data = data.replace('844', '488', 1)
        if '84' in data:
            data = data.replace('84', '3343', 1)
    if len(data) >= 20:
        print(len(data) >= 20, n)
