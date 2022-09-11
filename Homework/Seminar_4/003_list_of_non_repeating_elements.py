# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint

# Вариант 1 с использованием встроенного счетчика
def find_unique_values(numbers_list: list) -> list:
    result_list = []
    for i in numbers_list:
        if numbers_list.count(i) == 1:
            result_list.append(i)
    return result_list

# Вариант 2 без использования встроенного счетчика
# def find_unique_values_1(numbers_list: list) -> list:
#     result_list = []
    
#     for i in numbers_list: 
#         count = 0
#         for k in numbers_list:
#             if i == k:
#                 count += 1
#         if count == 1:
#             result_list.append(i)
#     return result_list


user_len_list = int(input("Введите длину числовой последовательности: "))
numbers_list = []

for i in range(user_len_list):
    numbers_list.append(randint(-user_len_list, user_len_list))
print(numbers_list)

print(find_unique_values(numbers_list))
# print(find_unique_values_1(numbers_list))
