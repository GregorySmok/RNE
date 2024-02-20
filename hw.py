with open('DATA/26-3.txt') as file:
    data = sorted([int(i) for i in file])
    space = 83960
can_save = []
for i in range(len(data)):
    if sum(can_save) + data[i] <= space:
        can_save.append(data[i])
print(len(can_save))