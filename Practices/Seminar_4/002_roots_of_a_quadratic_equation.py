# Ax² + Bx + C = 0
# х = −b/2a

import math


def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        # print("Действительных корней нет")
        return []
    
    elif discriminant == 0:
        # print(f' x = {-b / (2 * a)}')
        return [-b / (2 * a)]

    result_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    result_2 = (-b - math.sqrt(discriminant)) / (2 * a)
    # print(f'x_1 = {result_1}, x_2 = {result_2}')
    return [result_1, result_2]


print(square_root(-4, 28, -49)) # можно запросить у пользователя
