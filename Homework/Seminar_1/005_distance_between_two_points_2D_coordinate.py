from ast import Pow


def get_coordinate (point, number):
    print(f"Точка {number}")
    point.append(int(input("  Введите координату X: ")))
    point.append(int(input("  Введите координату Y: ")))
    return point


point_a, point_b = [], []
point_a = get_coordinate(point_a, 'A')
point_b = get_coordinate(point_b, 'B')

distance_between_two_points = round(((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5, 2)
print(f"Расстояние между точкой A({point_a[0]}, {point_a[1]}) и точкой B({point_b[0]}, {point_b[1]}) = {distance_between_two_points}")
