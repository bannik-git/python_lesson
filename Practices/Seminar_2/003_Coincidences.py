# user_string = input("Введите строку: ")
string_1 = "Я люблю питон!"
string_find = "лю"
count = 0
for i in range(len(string_1)):
    if string_1[i : i + len(string_find)] == string_find:
        count += 1
print(count)

# Вариант2
string_user = 'Я люблю питон'
counter = string_user.count('лю')
print(counter)

# Вариант 3
str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')

print(len(str1.split(str2)) - 1)
