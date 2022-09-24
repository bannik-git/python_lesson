# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;




# Вариант 1
#print(eval(user_str))

def f(function, a, b):
    return function(a, b)


def equation(string: str):
    if string == '+':
        return lambda a, b: a + b
    elif string == '*':
        return lambda a, b: a * b
    elif string == '/':
        return lambda a, b: a / b
    elif string == '-':
        return lambda a, b: a - b


def formation_of_numbers_in_left(index: int, user_str: str) -> int:
    'Формирование числа слева от знака'
    for k in range(len(user_str[:index])):
        if user_str[:index][-k -1] in '+-/*' and k != len(user_str[:index]) -1:
            index_2 = user_str.find(user_str[:index][-k -1])
            a = float(user_str[index_2 + 1 :index])
            return index_2, a
        elif k == len(user_str[:index]) - 1:
            index_2 = index
            a = float(user_str[:index])

    return index_2, a


def formation_of_numbers_in_right(index: int, user_str: str) -> int:
    'Формирование числа справа от знака'
    for k in range(len(user_str[index + 1:])):
        if user_str[index + 1:][k] in '+-/*':
            index_3 = (index + 1) + user_str[index + 1:].find(user_str[index + 1:][k])
            b = float(user_str[index + 1 : index_3])
            return index_3, b
        elif k == len(user_str[index + 1:]) - 1:
            index_3 = index
            b = float(user_str[index + 1:])
    return index_3, b


def string_formation(index: int, index_2: int, index_3: int, result: str, user_str: str) -> str:
    'формирование строки после вычисления'
    if index_3 == index_2 == index:
        return str(result)
    elif index_3 == index:
        return user_str[:index_2 + 1] + str(result)
    elif index_2 == index:
        return str(result) + user_str[index_3:]
    return user_str[:index_2 + 1] + str(result) + user_str[index_3:]


def calculation_logic(user_str:str, signs: str) -> str:
    'Логика вычисления'
    for i in user_str:
        if i in signs:
            index = user_str.find(i)

            index_2, a = formation_of_numbers_in_left(index, user_str)
            index_3, b = formation_of_numbers_in_right(index, user_str)
            res = f(equation(i), a, b)
            user_str = string_formation(index, index_2, index_3, res, user_str)
    return user_str


user_str = '2-3+2*3/5' 
user_str = calculation_logic(user_str, '/*')
user_str = calculation_logic(user_str, '+-')

print(user_str) 
