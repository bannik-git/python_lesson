def saving_numbers(a: int, b: int, operation: str):
    path = 'Practices/Seminar_7/Calc/numbers.txt'
    with open(path, 'a') as file:
        file.write(f'{a}{operation}{b}\n')

def reading_number()->str:
    path = 'Practices/Seminar_7/Calc/numbers.txt'
    with open(path, 'r') as file:
        return file.readlines()[-1]
