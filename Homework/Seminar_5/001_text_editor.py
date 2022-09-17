# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавуабв!'
# 'Мы очень любим Питон!'


base_str = 'Мы неабв очень любим Питон иабв Джавуабв!'
find_str = "абв"
result_str = ''

# Вариант 1: Стандартный метод
# for i in list(base_str.split()):
#     if 'абв' not in i:
#         result_str += i + " "

# print(result_str)

# Вариант 2: программа в одну строку.
result = " ".join([i for i in list(base_str.split()) if 'абв' not in i])
print(result)