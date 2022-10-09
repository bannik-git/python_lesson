import tkinter as tk
import gui, db


def start():
    check = db.check_file('Homework/Seminar_8/log.txt')
    if check:
        global path_open, content
        path_open = function_selection(('Homework/Seminar_8/log.txt',''), True)[-2]
        content = function_selection((path_open, ''), True)
        db.loger('запуск программы')
        gui.open_program(check, content)
    else:
        gui.open_program(check)
    

def open_file(header: tk.Frame):
    global path_open, content
    path_open = db.get_open_path()
    content = function_selection(path_open, True)
    gui.rendering(header, content)


def function_selection(path: str | tuple, read_or_write: bool) -> list[str]:
    'В зависимости от формата выбирает какую функцию запускать'
   
    if read_or_write: # read
        file_format = path[0].split('.')[-1]
        match file_format:
            case 'txt':
                return db.read_file_txt(path[0])
            case 'csv':
                return db.read_file_csv(path[0])
            case 'json':
                return db.read_file_json(path[0])
        
    else: # write
        if type(path) is tuple:
            file_format = path[0].split('.')[-1]
            path = path[0]
        else:
            file_format = path.split('.')[-1]
        match file_format:
            case 'txt':
                return db.write_file_txt(path, content)
            case 'csv':
                return db.write_file_csv(path, content)
            case 'json':
                return db.write_file_json(path, content)


def save_file():
    function_selection(path_open, False)


def save_as_file():
    path_new_file = db.get_save_path()
    function_selection(path_new_file, False)


def add_user(header: tk.Frame):
    gui.add_user_window(header)
   
def add_user_text(window: tk.Tk, new_user: str, header: tk.Frame):
    if new_user != '   ': # 3 пробела потому, что проблы вставлены после каждого заполянемого пункта, но последний убран срезом
        content.append(f'{int(content[-1][0]) + 1} {new_user}')
        db.loger(f'Добавлен новый пользователь {content[-1]}')
        gui.rendering(header, content)
    gui.close_window(window)


def delete(frame: tk.Frame, frame_button: tk.Frame, header: tk.Frame):
    gui.render_checkbox(frame, len(content), frame_button, header)


def delete_user(user_list: list[int], header: tk.Frame, delete_frame: tk.Frame, button : tk.Button, checkbox: list[tk.Label]):    
    buff = [content[0]]
    k = 1
    for i in range(len(user_list)):
        if user_list[i] == 0:
            buff.append(f'{k} {content[i + 1][2:]}')
            k += 1
            db.loger(f'Удаление пользователей: {k} {content[i + 1][2:]}')
    
    delete_frame.destroy()
    button.destroy()
    def object_destroy(object_destroy):
        for i in object_destroy: 
            i.destroy()

    object_destroy(checkbox)
    
    gui.rendering(header, buff)
    copy_list(buff)


def copy_list(buff):
    global content
    content = buff.copy()

def edit(frame: tk.Frame, frame_button: tk.Frame, header: tk.Frame):
    gui.render_checkbox(frame, len(content), frame_button, header, False)


def edit_user(user_list: list[int], header: tk.Frame, delete_frame: tk.Frame, button : tk.Button, checkbox: list[tk.Label]):
    global frame_delete, delete_button, delete_checkbox
    frame_delete = delete_frame
    delete_button = button
    delete_checkbox = checkbox

    for i in user_list:
        if i != 0:
            gui.add_user_window(header, content[i], i)


def replace_content(window: tk.Tk, new_user: str, user_index, header: tk.Frame):

    content[user_index] = f'{user_index} {new_user}'

    frame_delete.destroy()
    delete_button.destroy()
    
    
    def object_destroy(object_destroy):
        for i in object_destroy: 
            i.destroy()

    object_destroy(delete_checkbox)

    gui.rendering(header, content)
    window.destroy()

def close(window: tk.Tk):
    if type(path_open) is tuple: 
        db.loger(f'Закрытие программы \n{path_open[0]}')
    else:
        db.loger(f'Закрытие программы \n{path_open}')
    gui.close_window(window)
