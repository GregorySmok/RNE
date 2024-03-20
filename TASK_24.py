with open('DATA/24 (2).txt') as file:
    data = ' CABCABABABABCBA'.replace(
        'BAB', '*').replace('ABA', '*').split('C')
ml = 0
for el in data:
    ln = 0
    for i in range(len(el)):
        if el[i] == '*':
            ln += 1
        else:
            ln = 0
    ml = max(ml, ln)
print(data)
