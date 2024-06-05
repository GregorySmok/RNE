def seven(num):
    if num == 0:
        return '0'
    ans = ''
    while num != 0:
        ans += str(num % 7)
        num //= 7
    return ans[::-1]


d = 7 * 49**120 - 6 * 343**65 - 5 * 7**40
print(seven(d).count('6'))
