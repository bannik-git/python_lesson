number = float(input("Введите число: "))
print(int(number * 10) % 10)

# Альтернативное решение исползуя строки
number = input("Введите число: ")
print(number.split(".")[1][0])