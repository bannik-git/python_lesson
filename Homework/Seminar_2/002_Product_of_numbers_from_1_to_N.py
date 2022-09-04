from math import factorial

# Вариант 3 рекурсивная функция
# def factor (number):
#     if number == 1:
#         return 1
#     return factor(number -1) * number

user_number = int(input("Введите число: "))
result = []

for i in range(1, user_number + 1):
    result.append(factorial(i))

# Вариант 2 (без библиотек)
# for i in range(1, user_number + 1):
#     for j in range(1, i + 1):
#         factorial *= j
#     result.append(factorial)
#     factorial = 1

# Вариант 3: рекурсия
# for i in range(1, user_number + 1):
#     result.append(factor(i))

print(result)
