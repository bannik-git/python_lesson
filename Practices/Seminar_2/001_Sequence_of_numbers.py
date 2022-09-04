user_number = int(input("Введите число: "))
number = 1

for i in range(1, user_number + 1):
    if i != 1:
        number *= -3
    print(number, end = " ")
