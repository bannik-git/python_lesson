# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Формула Бэйли — Боруэйна — Плаффа
# пи = сумм(1/16^n*(4/(8*n+1)- 2/(8*n+4) - 1/(8*n +5) - 1/(8*n +6)))




def f(n):
    return (1 / 16 ** n) * ((4 / (8 * n + 1)) - (2 / (8 * n + 4)) - (1 / (8 * n + 5)) - (1/ (8 * n + 6)))

def round_up(number: int, accuracy: float) -> float:
    accuracy = len(accuracy.split('.')[1])
    divider = 1
    for i in range(accuracy):
        divider *= 10

    return number * divider // 1 / divider
        

accuracy = input("Введите необходимую точность: ").replace(",", ".")
n = 0
result = 0
switch = True
while switch:
    
    if (f(n - 1) - f(n)) > float(accuracy):
        result += f(n)
        n += 1
    else:
        switch = False


print(round_up(result, accuracy))
