import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


"""def compare_password(entered_password, hashed_password):
    entered_password_hashed = bcrypt.hashpw(
        entered_password.encode('utf-8'), hashed_password)
    return entered_password_hashed == hashed_password


entered_password = input("Введите ваш пароль: ")
hashed_password_from_database = b"hashed_password_from_database"

if compare_password(entered_password, hashed_password_from_database):
    print("Пароль верен.")
else:
    print("Пароль неверен.")"""

hashed_password = hash_password("123")
print(hashed_password)
