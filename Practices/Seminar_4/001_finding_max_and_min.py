user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")

for i in range(len(user_string)):
    user_string[i] = int(user_string[i])

# Более короткое преобразование   
# numbers = list(map(int, user_string))

print(f'max = {max(user_string)}, min = {min(user_string)}')
