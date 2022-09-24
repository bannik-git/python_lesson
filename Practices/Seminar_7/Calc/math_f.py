def equation(string: str, a: int, b: int):
    if string == '+':
        return summ(a, b)
    elif string == '-':
        return subtraction(a, b)
    elif string == '*':
        return multiply(a, b)
    elif string == '/':
        return division(a, b)


def summ(a: int, b: int) ->int:
    return a + b


def subtraction(a: int, b: int) ->int:
    return a - b


def multiply(a: int, b: int) ->int:
    return a * b


def division(a: int, b: int) ->float:
    return a / b
    