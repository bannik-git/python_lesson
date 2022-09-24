# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_of_numbers_of_odd_elements(number_list: list) -> int:
    sum_odd_element = 0
    for i in range(1, len(number_list), 2):
        sum_odd_element +=number_list[i]

    return sum_odd_element


user_list = [2, 3, 5, 9, 3]
# res = sum_of_numbers_of_odd_elements(user_list)

# Добавлена реализация через List comprehension
res = sum([user_list[i] for i in range(1, len(user_list), 2)])
print(res)