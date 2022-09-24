def number_request() -> int:
    return int(input('Введите число: '))

def operation_request() -> str:
    return input('Введите действие (+, -, *, /): ')

def output(a: int, b: int, operator: str, result: int | float):
    print(f'{a} {operator} {b} = {result}')