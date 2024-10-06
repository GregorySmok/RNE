with open('DATA/27-B_2.txt') as f:
    n = int(f.readline())
    d = [int(i) for i in f]
pref = 0
pref_2 = 0
pref_7 = 0
pref_14 = 0
m_ans = 0
for num in d:
    if num % 14 == 0:
        if pref != 0:
            m_ans = max(m_ans, num * pref)
        pref_14 = max(pref_14, num)
    elif num % 7 == 0:
        if pref_2 != 0:
            m_ans = max(m_ans, num * pref_2)
        pref_7 = max(pref_7, num)
    elif num % 2 == 0:
        if pref_7 != 0:
            m_ans = max(m_ans, num * pref_7)
        pref_2 = max(pref_2, num)
    else:
        if pref_14 != 0:
            m_ans = max(m_ans, num * pref_14)
    pref = max(pref, num)
print(m_ans)
