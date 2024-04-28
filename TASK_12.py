d = '>' + '1' * 10 + '2' * 20 + '3' * 30
while '>1' in d or '>2' in d or '>3' in d:
    if '>1' in d:
        d = d.replace('>1', '22>', 1)
    if '>2' in d:
        d = d.replace('>2', '2>', 1)
    if '>3' in d:
        d = d.replace('>3', '1>', 1)
s = 0
for e in d:
    if e.isdigit():
        s += int(e)
print(s)