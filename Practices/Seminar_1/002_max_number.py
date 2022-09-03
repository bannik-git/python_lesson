amount_of_numbers = 5
number_list = []

for i in range(amount_of_numbers):
    number_list.append(int(input("Введите число: ")))

# Часть кода ниже можно заменить на print(max(number_list))

max_number = number_list[0]

for number in range(1, amount_of_numbers):
    
    if max_number < number_list[number]:
        max_number = number_list[number]

print(max_number)