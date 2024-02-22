x, y = 0, 0
mn = 1
st = input()
count = 1
while '#' not in st:
    if len(st) != 0:
        if 'for' in st:
            mn = int(st[st.find('(') + 1:st.find(')')])
        else:
            if '    ' not in st:
                mn = 1
            if st[st.find('(') + 1:st.find(')')].isdigit():
                count = int(st[st.find('(') + 1:st.find(')')])
            else:
                count = 1
            if 'up' in st:
                y += 1 * mn * count
            if 'down' in st:
                y -= 1 * mn * count
            if 'left' in st:
                x -= 1 * mn * count
            if 'right' in st:
                x += 1 * mn * count
    count = 1
    st = input()
if x > 0:
    print(f'move_right({x})' if x != 1 else 'move_right()')
elif x < 0:
    print(f'move_left({x})' if x != -1 else 'move_right()')
else:
    print()
if y > 0:
    print(f'move_up({y})' if y != 1 else 'move_up()')
elif y < 0:
    print(f'move_down({abs(y)})' if y != -1 else 'move_down()')
else:
    print()
