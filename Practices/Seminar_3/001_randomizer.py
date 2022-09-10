# Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

import time

def my_random(minn, maxx):
    time.sleep(0.3)
    return int((time.time() % 1  * (maxx - minn)) + minn)


for i in range(10):
    print(my_random(1, 9))

# Вариант №2
# def random(a,b):
#     the_set = set()
#     list = []
#     for i in range(a,b):
#         the_set.add(str(i))

#     for e in the_set:
#         list.append(e)
#     print(list)

# random(5, 10)

# Вариант №3
# import time

# def random():
#     interval = int(input('Введите желаемый интервал рандома: '))
#     ms = time.time()*1000.0
#     b = int(ms)
#     d = ms - b
#     answer = d * interval
#     print(int(round(answer, 0)))
#     return answer

# random()
