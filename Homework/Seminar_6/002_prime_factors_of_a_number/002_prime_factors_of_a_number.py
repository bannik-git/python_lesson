
def prime_factors_of_a_number(user_number: int, prime_number: list[int]) -> str:
    switch = True
    result = ''
    while switch:
        if user_number == 1:
            switch = False
        for i in prime_number:
            if user_number % i == 0:
                result += f'{i} '
                user_number //= i
                break 
        if user_number in prime_number:
            result += f'{int(user_number)}'
            switch = False
        
    return result


with open('C:/Users/admin/Desktop/GeekBrains/Python/Homework/Seminar_4/002_prime_factors_of_a_number/prime_numbers.txt', 'r') as file:
    prime_number = file.read().replace("\n", ', ').split(', ')



# for i in range(len(prime_number)):
#     prime_number[i] = int(prime_number[i])

# Реализация через map()
prime_number = list(map(int, prime_number))

user_number = int(input("Введите целое число: "))
print(prime_factors_of_a_number(user_number, prime_number))
