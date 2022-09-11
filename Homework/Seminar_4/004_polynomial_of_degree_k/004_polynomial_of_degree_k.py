# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

def polynomial_creation(degree: int) -> str:
    polynomial_arguments = ''
# user_degree +1  потому что aх^2 + bx + c = 0 
    for i in range(degree + 1):
        if i < (degree - 1): 
            polynomial_arguments += f'{randint(0, 100)}*x^{degree - i} + '
        elif i == (degree - 1):
            polynomial_arguments += f'{randint(0, 100)}*x + '
        else:
            polynomial_arguments += f'{randint(0, 100)} = 0'

    return polynomial_arguments


user_degree = int(input('Введите степень: '))

with open("Homework/Seminar_4/004_polynomial_of_degree_k/polynomial.txt", 'a') as file:
    file.write(f'\n{polynomial_creation(user_degree)}')
