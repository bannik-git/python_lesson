# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

def product_of_pairs_of_numbers(number_list: list) -> list:
    res_list = []
    for i in range(ceil(len(number_list)/2)):
        res_list.append(number_list[i] * number_list[-i -1])
    return res_list


user_int_list = [2, 3, 5, 6]
res_list = product_of_pairs_of_numbers(user_int_list)
print(res_list)
