# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Формула Бэйли — Боруэйна — Плаффа
# пи = сумм(1/16^n*(4/(8*n+1)- 2/(8*n+4) - 1/(8*n +5) - 1/(8*n +6)))


from decimal import Decimal, ROUND_FLOOR


def f(n):
    return Decimal((1 / 16 ** n) * ((4 / (8 * n + 1)) - (2 / (8 * n + 4)) - (1 / (8 * n + 5)) - (1/ (8 * n + 6))))


accuracy = Decimal(input("Введите необходимую точность: ").replace(",", "."))
n = 0
result = Decimal(0)
switch = True
while switch:
    
    if (f(n - 1) - f(n)) > accuracy:
        result += f(n)
        n += 1
    else:
        switch = False

print(result.quantize(Decimal('0.' + n * '0'), ROUND_FLOOR))
