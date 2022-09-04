from random import randint

user_number = int(input("Введите число: "))
user_list = []

for i in range(user_number):
    user_list.append(randint(-user_number, user_number))

print(f"\nВаш список - {user_list}")

user_index = input("""\nВведите индексы элементов произведение которых Вы хотите получить
последовательность чисел вводить через пробел: """)

index = user_index.split(" ")
result = user_list[int(index[0])]

for i in range(1, len(index)):
    result *= user_list[int(index[i])]

print(result)
