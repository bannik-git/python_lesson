day_of_the_week = input("Введите порядковый номер дня недели: ")

# можно сделать через цифры и лист [6, 7] или 6 <= day_of_the_week <= 7
if day_of_the_week in '67': 
    print("Да")
else:
    print("Нет")
