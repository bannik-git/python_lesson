quarter_coordinate_number = int(input("Введие номер четверти координат: "))

if quarter_coordinate_number == 1:
    print("Значение Х > 0 и У > 0")
elif quarter_coordinate_number == 2:
    print("Значения Х < 0 и У > 0")
elif quarter_coordinate_number == 3:
    print("Значения Х < 0 и У < 0")
elif quarter_coordinate_number == 4:
    print("Значения Х > 0 и У < 0")
else:
    print("Номер четверти не может быть > 4")