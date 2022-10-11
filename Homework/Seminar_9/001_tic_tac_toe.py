from itertools import count
from tkinter import *
import tkinter
from tkinter import messagebox
 
height_w = 320
width_w = 250
window = Tk()
window.geometry(f'{height_w}x{width_w}')


def start_game():

    global btk_1, btk_2, count_of_moves, user_char 
    count_of_moves = 0
    user_char = True
    btk_1 = Button(master=window, text='Игра против пользователя', command = lambda x = False: start_new_game(x))
    btk_2 = Button(master=window, text='Игра против компьютера', command = lambda x = True: start_new_game(x))
    btk_1.place(relx=0.2, rely=0.2, relheight=0.2 ,relwidth=0.6)
    btk_2.place(relx=0.2, rely=0.5, relheight=0.2 ,relwidth=0.6)
    

def сonclusion_of_the_winner(button_list: list, char: list = ['O']):
    if victory(button_list, char):
        if messagebox.askokcancel("Победа", f'Победил {char}'):
            for i in button_list:
                i.destroy()                
            start_game()
        else:
            window.destroy()


def victory(button_list: list, char: list = ['O']) -> bool:
    'Проверка на победу после хода'
    victory_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in victory_list:
        if button_list[i[0]]['text'] == button_list[i[1]]['text'] == button_list[i[2]]['text'] == char[0]:
            return True
    return False


def winning_moves(button_list: list, char: str)-> tuple:
    'Проверка наличия победного хода'
    сhecklist = [[0, 1], [1, 2], [2, 0], 
                [3, 4], [4, 5], [3, 5], 
                [6, 7], [7, 8], [6, 8],
                [1, 4], [4, 7], [7, 1], 
                [2, 5], [5, 8], [8, 2], 
                [0, 4], [4, 8], [8, 0],
                [2, 4], [4, 6], [2, 6], 
                [0, 3], [3, 6], [0, 6],
                [2, 5], [5, 8], [2, 8]]   
    return_move = [[2, 0, 1], [5, 3, 4], [8, 6, 7], [7, 1, 4], [8, 2, 5], [8, 0, 4], [6, 2, 4],
    [6, 0, 3], [8, 2, 5]]
    count = 0
    k = 0
    for i in range(len(сhecklist)):
        if button_list[сhecklist[i][0]]['text'] == button_list[сhecklist[i][1]]['text'] == char\
            and button_list[return_move[count][k]]['text'] != 'O':
            return (True, return_move[count][k])
        k += 1
        if k == 3:
            count += 1
            k = 0

    return (False, False)


def user_move_to_corner(button_list: list)-> bool:
    'Проверка что пользователь не занял угол'
    index_move = [8, 6, 2, 0]
    corners = [0, 2, 6, 8]
    for i in range(len(corners)):
        if button_list[corners[i]]['text'] == 'X':
            return (i, index_move[i])
    return (False, False)


def move_computer(button_list: list, count_of_moves: int):
    winner_computer = winning_moves(button_list, 'O')
    winner_user = winning_moves(button_list, 'X')

    if count_of_moves <= 1:
        user_move = user_move_to_corner(button_list)
        if button_list[4]['text'] != 'X':
            put_up_a_sign(4, button_list, 'O')
        elif user_move[0] in (0, 2, 6, 8):
            put_up_a_sign(user_move[1], button_list, 'O')

    elif winner_computer[0] and button_list[winner_computer[1]]['text'] != 'X':
        put_up_a_sign(winner_computer[1], button_list, 'O')
    elif winner_user[0]:
        put_up_a_sign(winner_user[1], button_list, 'O')
    else:
        if button_list[0]['text'] == button_list[8]['text'] == 'X' \
            or button_list[2]['text'] == button_list[6]['text'] == 'X':
            put_up_a_sign(5, button_list, 'O')
        elif button_list[7]['text'] == button_list[5]['text'] == 'X' and button_list[8]['text'] != 'O':
            put_up_a_sign(8, button_list, 'O')
        else:
            for i in (0, 2, 6, 8):
                if button_list[i]['text'] == '':
                    put_up_a_sign(i, button_list, 'O')
                    break
            else:
                for i in range(9):
                    if button_list[i]['text'] == '':
                        put_up_a_sign(i, button_list, 'O')
                        break
    
    
def put_up_a_sign(index: int, button_list: list, char: str):
    button_list[index].configure(text = char)
    button_list[index]['state']= tkinter.DISABLED
    button_list[index]['relief'] = tkinter.SUNKEN


def clik(index: int, button_list: list, enemy: bool):
    global user_char, count_of_moves, user_char
    
    put_up_a_sign(index, button_list, ['X' if user_char else 'O'])
    count_of_moves += 1
    сonclusion_of_the_winner(button_list, ['X' if user_char else 'O'])
 
    if enemy:
        move_computer(button_list, count_of_moves)
        count_of_moves += 1
        сonclusion_of_the_winner(button_list)
    else:
        if count_of_moves != 0:
            user_char = not user_char

    if count_of_moves >= 9:
        if messagebox.askokcancel("Ничья", 'Вы молодец!'): 
                for i in button_list:
                    i.destroy()                
                start_game()
        else:
            window.destroy()
        

def start_new_game(enemy: bool):
    btk_1.destroy()
    btk_2.destroy()
    button_list = [0 for x in range(9)]
    for i in range(9):

            button_list[i] = Button(master=window, text='', command=lambda index = i,:clik(index, button_list, enemy))
            button_list[i].place(relx=0.2, rely=0.2, relheight=0.2 ,relwidth=0.6)
    index = 0
    for i in range(3):
        for k in range(3):
            button_list[index].place(relx=0.005 + k * 0.33, rely=i * 0.33, relheight=0.33 ,relwidth=0.33)
            index += 1


start_game()

window.mainloop()
