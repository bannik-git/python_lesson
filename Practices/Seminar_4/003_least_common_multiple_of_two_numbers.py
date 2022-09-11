# number_1 = 126 
# number_2 = 70

def NOD(a:int, b:int) -> int:
    while True:
        if a > b:
            a = a - b
        else:
            b = b - a

        if a % b == 0:
            return b
        elif b % a == 0:
            return a


def NOK(a:int, b:int) -> int:
        return int((a * b) / NOD(a,b))


print(NOK(84, 648)) # Цифры можно запросить у пользователя


# Вариант 2
# import math
# a = int(input("a = "))
# b = int(input("b = "))
# print(math.lcm(a, b))

