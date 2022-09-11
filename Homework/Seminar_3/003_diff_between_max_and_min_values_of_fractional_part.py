# # Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# # Пример:

# # - [1.1, 1.2, 3.1, 10.01] => 0.19


def diff_between_max_and_min_values_of_fractional_part(number_list: list) -> float:
    result_list = []
    for i in number_list:
        # if str(i).split(".")[1] != '0': Если надо исключить 0 из расчета
        result_list.append(float('0.' + str(i).split(".")[1]))
    
    return max(result_list) - min(result_list) 


user_number_list = [1.1, 1.2, 3.1, 10.01]
result = diff_between_max_and_min_values_of_fractional_part(user_number_list)
print(result)
