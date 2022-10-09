from tkinter import filedialog
import csv, json, time, os


def check_file(path: str)-> bool:
    return os.path.isfile(path)


def get_open_path():
    return filedialog.askopenfilenames(filetypes=(("all file", "*.*"), ("text files", "*.txt"), ("csv files", "*.csv"), ("json file", "*.json")))


def get_save_path():
    return filedialog.asksaveasfilename(defaultextension=".*", filetypes=(("all file", "*.*"), ("text files", "*.txt"), ("csv files", "*.csv"), ("json file", "*.json")))


def read_file_txt(path):
    with open(path, 'r') as txtfile:
        reader = txtfile.read().split('\n')
    loger(f'чтение файла txt путь {path}')
    return reader


def read_file_csv(path):
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';',dialect='excel')
        buff_list = []
        for i in reader:
            if i != '':
                buff_list.append(' '.join(i))
    loger(f'чтение файла csv путь {path}')
    return buff_list


def read_file_json(path):
    with open(path) as jsonfile:
        reader = json.load(jsonfile)
    loger(f'чтение файла json путь {path}')
    return reader


def write_file_txt(path: str, content: list[str]):
    with open(path, 'w') as txtfile:
        for i in content:
            if i != '':
                txtfile.write(i + '\n')
    loger(f'запись файла txt путь {path}')


def write_file_csv(path: str, content: list[str]):
    buff_list = []
    for i in content:
        if i != '':
            buff_list.append(i.split())
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=';', quotechar=' ')
        writer.writerows(buff_list)
    loger(f'запись файла csv путь {path}')


def write_file_json(path: str, content: list[str]):
    with open(path, 'w') as jsonfile:
        jsonfile.write(json.dumps(content))
    loger(f'запись файла json путь {path}')


def loger(string: str):
    with open('Homework/Seminar_8/log.txt', 'a') as file:
        file.write(f'{time.ctime()}: {string}\n')
        