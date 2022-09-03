while True:
    coordinate_x = int(input("Введите координату Х: "))
    coordinate_y = int(input("Введите координату У: "))

    if (coordinate_x > 0) and (coordinate_y > 0):
        print("Четверть №1")
    elif (coordinate_x > 0) and (coordinate_y < 0):
        print("Четверть №4")
    elif (coordinate_x < 0) and (coordinate_y > 0):
        print("Четверть №2")
    elif (coordinate_x < 0) and (coordinate_y < 0):
        print("Четверть №3")
    else:
        print("Координаты Х и У не должны быть равны 0")
        continue
    
    break