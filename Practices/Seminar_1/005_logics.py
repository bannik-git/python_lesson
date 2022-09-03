number = int(input("Введите число: "))

if ((number % 5 == 0) and (number % 10 == 0)) or ((number % 15 == 0) and not(number % 30 == 0)):
# Условие можно сократить до if (number % 10 == 0) or (number % 15 == 0) 
    print("да")
else:
    print("нет")