import view, math_f, db


def сalculator():

    number_1 = view.number_request()
    number_2 = view.number_request()
    operator = view.operation_request()

    db.saving_numbers(number_1, number_2, operator)
    numbers = tuple(map(int, db.reading_number().split(operator)))

    result = math_f.equation(operator, numbers[0], numbers[1])
    view.output(numbers[0], numbers[1], operator, result)
