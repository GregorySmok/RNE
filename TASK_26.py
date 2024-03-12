with open('DATA/26 (4).txt') as f:
    data = [int(i) for i in f]
updated = [data[0]]
for i in range(1, len(data) - 1):
    updated.append(sorted([data[i-1], data[i], data[i + 1]])[1])
updated.append(data[-1])
water = 0
for i in range(len(data)):
    if updated[i] < data[i]:
        water += data[i] - updated[i]
print(updated.count(min(updated)), water)
