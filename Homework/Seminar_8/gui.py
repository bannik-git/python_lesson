import tkinter as tk
from tkinter import Menu, messagebox
import controller

def rendering(header_win: tk.Frame, content: list[str]):
    global new_frame
    new_frame = tk.Frame(header_win)
    new_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
    for i in range(len(content)):
        buff_str = content[i].split()
        for k in range(len(buff_str)):
            tk.Label(master = new_frame, text=buff_str[k]).place(relx=0.005 + k * 0.18, rely= i * 0.05, relheight=0.05 ,relwidth=0.18)


def render_checkbox(frame: tk.Frame, count_row: int, frame_button: tk.Frame, header: tk.Frame, del_or_edit: bool = True):
    'Отрисовка чекбоксов'
    cb_list = []
    button = []
    def check_button(i):
        
        cb = tk.Checkbutton(frame, variable = button[i - 1], onvalue=i, offvalue=0)
        cb.place(relx=0.5, rely= 0.05 * i, relwidth=0.3, relheight=0.05)
        cb_list.append(cb)

    for i in range(1, count_row):
        button.append(tk.IntVar())
        check_button(i)
        
    
    def delete():
        buff_list = []
        for i in button:
            buff_list.append(i.get())
        controller.delete_user(buff_list, header, new_frame, del_button, cb_list)


    def edit():
        buff_list = []
        for i in button:
            buff_list.append(i.get())
        controller.edit_user(buff_list, header, new_frame, del_button, cb_list)


    if del_or_edit:
        del_button = tk.Button(frame_button, text="Удалить", command = delete)
        del_button.place(relx = 0, rely = 0, relwidth=1, relheight=1)
    else:
        del_button = tk.Button(frame_button, text="Редактировать", command = edit)
        del_button.place(relx = 0, rely = 0, relwidth=1, relheight=1)
  

def add_user_window(header, user = '', user_index = 0):

    def read():
        buff_list = ''
        for i in entry_list:
            buff_list += i.get() + ' '
        controller.add_user_text(new_window, buff_list[:-1], header)
    
    def edit_user():
        buff_list = ''
        for i in entry_list:
            buff_list += i.get() + ' '
        controller.replace_content(new_window, buff_list[:-1], user_index, header)


    new_window = tk.Tk()
    new_window.title('Добавление пользователя')
    new_window.geometry('300x130')  
    field_list = ['Имя', 'Фамилия', 'Телефон', 'Примечание']
    entry_list = []
    if user == '':
        for i in range(len(field_list)):
            tk.Label(master=new_window, text= field_list[i], width=15, height=1).grid(row = i, column= 1)
            k = tk.Entry(master=new_window, width=30)
            k.grid(row=i, column=2)
            entry_list.append(k)
        buttun = tk.Button(master=new_window, text='Добавить', command = read)
        buttun.grid(row=5, column=2)
    else:
        user_list = user.split()
        for i in range(len(field_list)):
            tk.Label(master=new_window, text= field_list[i], width=15, height=1).grid(row = i, column= 1)
            k = tk.Entry(master=new_window, width=30)
            k.insert(0, user_list[i + 1])
            k.grid(row=i, column=2)
            entry_list.append(k)
        buttun = tk.Button(master=new_window, text='Изменить', command = edit_user)
        buttun.grid(row=5, column=2)


    


    # buttun = tk.Button(master=new_window, text='Добавить', command = read)
    # buttun.grid(row=5, column=2)
    
    new_window.mainloop()


def show_after():
    messagebox.showinfo("О телефонном справочнике", "Создан в рамках выполнения домашнего задания по python в 2022 году.")


def close_window(window):
    window.destroy()


def on_closing(window):
    controller.close(window)


def open_program(check: bool, content: list[str] = ''):

    window = tk.Tk()
    window.title("Телефонный справочник")
    window.geometry('700x400')
    header_win = tk.Frame(master = window)
    header_win.place(relx= 0.05, rely = 0, relheight= 1, relwidth=0.95)

    check_box_win = tk.Frame(master=window)
    check_box_win.place(relx=0, rely= 0, relheight=1 ,relwidth=0.1)

    button_frame = tk.Frame(window)
    button_frame.place(relx = 0, rely= 0.85, relwidth=1, relheight= 0.15)

    menu = Menu(window)
    file = Menu(menu, tearoff=0)
    file.add_command(label= "Открыть файл", command = lambda x = header_win: controller.open_file(x))
    file.add_command(label= "Сохранить", command = controller.save_file)
    file.add_command(label= "Сохранить как", command = controller.save_as_file)

    file.add_command(label= "Выход", command = lambda x = window: controller.close(x))
    menu.add_cascade(label = 'Файл', menu = file)


    user = Menu(window)
    user = Menu(user, tearoff=0)
    user.add_command(label="Добавить пользователя", command = lambda x = header_win: controller.add_user(x))
    user.add_command(label="Удалить пользователя", command =lambda x = check_box_win, y = button_frame, z = header_win: controller.delete(x, y, z))
    user.add_command(label="Редактировать пользователя", command = lambda x = check_box_win, y = button_frame, z = header_win: controller.edit(x, y, z))

    menu.add_cascade(label="Пользователи", menu = user)


    after = Menu(window)
    after = Menu(after, tearoff=0)
    after.add_command(label="О телефонном справочнике", command = show_after)


    menu.add_cascade(label= "Справка", menu = after)
    window.config(menu=menu)
    def on_closing():
        controller.close(window)

    if check:
        rendering(header_win, content)

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()