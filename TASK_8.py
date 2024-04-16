from itertools import product

count = 0
for el in product('аёртш', repeat=5):
    count += 1
    st = ''.join(el)
    print(count, st)
    if st.count("а") <= 1 and 'ёё' not in st:
        print(count)
        break
