# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import os


def move_player(player: int, leftover_candy: int, complexity:int = 0) -> int:
    'Функция запрашивающая кол-во конфет у пользователя'
    if player == 'Компьютер':
        if complexity == 1:
            return easy_enemy_move(leftover_candy)
        return hard_enemy_move(leftover_candy)
    else:
        while True:
            user_candy = input(f'Ходит {player}: ')
            if user_candy.isdigit():
                if 0 < int(user_candy) < 29:
                    return int(user_candy)
                else:
                    print('За один ход можно забрать от 1 до 28 конфет')
            else:
                    print('За один ход можно забрать от 1 до 28 конфет')


def easy_enemy_move(leftover_candy:int) -> int:
    'Логика простого компьютера'
    if leftover_candy > 28:
        return randint(1, 28)
    else:
        computer_move = randint(1, 28)
        while not (leftover_candy - computer_move >= 1): 
            computer_move = randint(1, 28)
        return computer_move


def hard_enemy_move(leftover_candy: int) -> int:
    'Логика компьютера который не прощает ошибок'
    if leftover_candy > 57:
        if leftover_candy % 29 == 0:
            return 5
        return int(leftover_candy % 29) 
    elif 29 <leftover_candy <= 57:
        return leftover_candy - 30
    return leftover_candy - 1
    

def user_name(number_user: int) -> str:
    'Функция запрашивающая имя пользователя'
    if number_user == 0:
        return input('Введите Ваше имя: ')
    elif number_user == 1:
        return input('Введите имя первого игрока: ')
    return input('Введите имя второго игрока: ')


sweets = 2021
stroke_detection = randint(0, 1)

os.system('cls')


print(""" Добрый день.
Вас приветствует игра Конфетки.

Правила:
        На столе лежит 2021 конфета.
        За один ход можно забрать от 1 до 28 конфет.
Цель игры:
         Заставить оппанента забрать последнюю конфету.
Опции:
        Вы можете выбрать противника:
        1 - хотите играть с другом
        2 - хотите играть против компьютера\n""")

enemy = int(input('C кем Вы хотите играть: '))
user_1 = (user_name(1) if enemy == 1 else user_name(0))
user_2 = (user_name(2) if enemy == 1 else 'Компьютер')

if enemy != 1:
    complexity = int(input('''Выбор сложности: 
        1 - простой
        2 - очень сложный (только для опытных игроков)
        Какой выбирате: '''))

while sweets > 1:
    
    if enemy == 2:
        if complexity == 1:
            comp_move = move_player(user_1 if stroke_detection else user_2, sweets, complexity)
        else:
            comp_move = move_player(user_1 if stroke_detection else user_2, sweets, complexity)
        
        print(f'Ход компьютера: {comp_move}')
        sweets -= comp_move
    
    else:
        sweets -= move_player(user_1 if stroke_detection else user_2, sweets)
    
    stroke_detection = not stroke_detection
    print(f'Количество конфет = {sweets}')

else:
    print(f'Победил {user_2 if stroke_detection else user_1}')

