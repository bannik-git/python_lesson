user_number = int(input("Введите число: "))
user_list = []

for i in range(1, user_number + 1):
    user_list.append((1 + 1/i)**i)

print(sum(user_list))
