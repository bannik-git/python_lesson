# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negative_fibonacci(sequence_size: int) -> list:
    
    positive_sequence = [1, 1]
    for i in range(2, sequence_size):
        positive_sequence.append(positive_sequence[i-1] + positive_sequence[i-2])  

    negative_sequence = positive_sequence.copy()
    for i in range(1, len(negative_sequence), 2):
        negative_sequence[i] *= -1
    negative_sequence.reverse()

    return negative_sequence + [0] + positive_sequence

amount_of_elements = int(input('Введите количество элементов: '))
print(negative_fibonacci(amount_of_elements))


