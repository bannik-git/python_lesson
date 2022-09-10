# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_convertion(number: int) -> str:
    if number // 2 == 0:
        return str(number)
    
    return str(binary_convertion(number//2))+ str(number % 2)


user_number = int(input('Введите число: '))
print(binary_convertion(user_number))
