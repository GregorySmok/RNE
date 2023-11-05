for n in range(100, 201):
    for m in range(100, 201):
        for k in range(100, 201):
            data = '>'+k*'0'+m*'1'+n*'2'
            while '>1' in data or '>2' in data or '>0' in data:
                if '>1' in data:
                    data = data.replace('>1', '20>')
                if '>2' in data:
                    data = data.replace('>2', '00>')
                if '>0' in data:
                    data = data.replace('>0', '10>')
            s = 0
            for el in data:
                if el.isdigit():
                    s += int(el)
            if s == 599:
                print(k)
