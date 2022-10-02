import view, contact_handler, db, os


def work(path: str, dict_fieldnames: dict, fieldnames: list):
    while True:

        аction = view.data_request('''
    1 - Добавление пользователя
    2 - Поиск пользователей
    3 - Редактирование пользователя
    4 - Удаление пользователя
    5 - Вывод всех пользователей
    6 - Экспорт базы в .txt
    7 - Импорт базы
    8 - Выход
Введите действие которое хотите выполнить: ''')
        match аction:
            case '1':
                add_new_user(path, fieldnames)
            case '2':
                search_user(path, dict_fieldnames, fieldnames)
            case '3':
                edit_user(path, dict_fieldnames, fieldnames)
            case '4':
                delete_user(path, dict_fieldnames, fieldnames)
            case '5':
                print_all_users(path, fieldnames)
            case '6':
                export_file(path, fieldnames)
            case '7':
                import_file(path, dict_fieldnames, fieldnames)
            case '8':
                break


def add_new_user(path, fieldnames):
    user_first_name = view.data_request('Введите имя контакта: ')
    user_second_name = view.data_request('Введите фамилию контакта: ')
    user_phone = view.data_request('Введите телефон контакта: ')
    user_note = view.data_request('Введите примечание к контакту: ')
    
    user_list = db.read_file_csv(path)
    check_file = os.path.isfile(path)
    new_user_dict = contact_handler.user_dictionary(check_file, user_list, user_first_name, user_second_name, user_phone, user_note)
    db.adding_data_to_the_database_csv(new_user_dict, check_file, path, fieldnames)


def edit_user(path, dict_fieldnames, fieldnames):
    user = view.data_request('Введите идентификатор пользователя: ')
    search_field = int(view.data_request('Введите поле для поиска (1 - Имя, 2 - Фамилия, 3 - Телефон, 4 - Примечание): '))
    what_to_edit = list(map(int, view.data_request('Введите через пробел что хотите редактировать (1 - Имя, 2 - Фамилия, 3 - Телефон, 4 - Примечание, 5 - все поля): ').split()))
    users = db.read_file_csv(path)
    searched_users = contact_handler.find_user(users, user, search_field, dict_fieldnames)
    
    id_user = contact_handler.get_id_user(searched_users, fieldnames)
    user_list = contact_handler.edit_user(users, id_user, what_to_edit, dict_fieldnames)
    db.overwriting_file_csv(user_list, path, fieldnames)


def search_user(path: str, dict_fieldnames: dict, fieldnames: list):

    user = view.data_request('Введите идентификатор пользователя: ')
    search_field = int(view.data_request('Введите поле для поиска (1 - Имя, 2 - Фамилия, 3 - Телефон, 4 - Примечание): '))
    
    users = db.read_file_csv(path)
    searched_users = contact_handler.find_user(users, user, search_field, dict_fieldnames)
    view.print_user(searched_users, fieldnames)


def delete_user(path:str, dict_fieldnames: dict, fieldnames: list[str]):
    user = view.data_request('Введите идентификатор пользователя: ')
    search_field = int(view.data_request('Введите поле для поиска (1 - Имя, 2 - Фамилия, 3 - Телефон, 4 - Примечание): '))
    users = db.read_file_csv(path)
    searched_users = contact_handler.find_user(users, user, search_field, dict_fieldnames)
    id_user = contact_handler.get_id_user(searched_users, fieldnames)
    user_list = contact_handler.delete_user(users, id_user)
    db.overwriting_file_csv(user_list, path, fieldnames)


def print_all_users(path: str, fieldnames: list):
    users = db.read_file_csv(path)
    view.print_user(users, fieldnames)


def import_file(path: str, dict_fieldnames: dict, fieldnames: list[str]):
    name_txt_file = view.data_request('Укажите имя файла: ')
    path_file = view.data_request('Укажите путь к файлу: ').replace('\\', '/')
    user_list_txt = db.read_file_txt(f'{path_file}/{name_txt_file}')
    new_user_list_dict = contact_handler.data_preparation_user_in_csv(user_list_txt, dict_fieldnames)
    check_file = os.path.isfile(path)
    for i in new_user_list_dict:
        user_list = db.read_file_csv(path)
        user_dict = contact_handler.user_dictionary(check_file, user_list, i[dict_fieldnames[1]], i[dict_fieldnames[2]], i[dict_fieldnames[3]], i[dict_fieldnames[4]])
        db.adding_data_to_the_database_csv(user_dict, check_file, path, fieldnames)


def export_file(path, fieldnames):
    user_list = contact_handler.data_preparation_user_in_txt(db.read_file_csv(path))
    fieldnames_str = contact_handler.data_preparation_fieldnames_in_txt(fieldnames)
    name_file = view.data_request('Укажите имя файла: ')
    path_file = view.data_request('Укажите путь куда хотите сохранить файл: ').replace('\\', '/')
    
    db.export_file_txt(name_file, path_file, user_list, fieldnames_str)
    