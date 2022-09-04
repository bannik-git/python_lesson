# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11


user_number = input("Введите дробное число: ")
result = 0
number_list = user_number.replace(".", ",").split(",")

for i in number_list:
    for j in range(len(i)):
        result += int(i[j])

print(result)
