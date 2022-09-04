from random import randint, shuffle

user_number = int(input("Введите число: "))
user_list = []

for i in range(user_number):
    user_list.append(randint(-user_number, user_number))

print(f"\nВаш список - {user_list}")

# Вариант 1 метод библиотеки random
# shuffle(user_list)

# Вариант 2 самописный алгоритм
index_list = []
result_list = []
while len(index_list) != len(user_list):
    index = randint(0, len(user_list) - 1)
    if not(index in index_list):
        index_list.append(index)

for i in index_list:
    result_list.append(user_list[i])

print(f"Перемешанный список - {result_list}")