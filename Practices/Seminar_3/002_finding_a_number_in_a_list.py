# Задайте список. Напишите программу, которая определит, присутствует ли
#  в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

def search_str(base_string, find_str):
    list_res = []
    for i in base_string:
        if find_str in i:
            list_res.append(i)
    return list_res


list_1 = ['efg23', '79234gefg', 'sdgs', 'g53']
find_str = '2'

list_res = search_str(list_1, find_str)

print(list_res)
