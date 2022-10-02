import csv, os.path
# работа с базой


def read_file_csv(path: str) -> list[dict]:
    if os.path.isfile(path):
        user_list =[]
        with open (path, 'r') as csvfile:
            name_reader = csv.DictReader(csvfile, delimiter=";")
            for i in name_reader:
                user_list.append(i)
            return user_list
    return -1


def read_file_txt(path: str) -> list[str]:
    if os.path.isfile(path):
        user_list = []
        with open(path, 'r') as txtfile:
            file_reader = txtfile.readlines()
            for i in range(1, len(file_reader)):
                user_list.append(file_reader[i])
        return user_list
    return -1


def overwriting_file_csv(user_list: list, path: str, fieldnames: list):
    with open(path, 'w', newline='') as csvfile:
        name_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', dialect='excel-tab')
        name_dict_writer.writeheader()
        for i in user_list:
            name_dict_writer.writerow(i)


def adding_data_to_the_database_csv(user_dict: dict, check_file: bool, path: str, fieldnames: list):
       
    with open(path, 'a', newline='') as csvfile:
        name_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', dialect='excel-tab')
        if not(check_file):
            name_dict_writer.writeheader()
        for i in user_dict:
            name_dict_writer.writerow(i)


def export_file_txt(file_name: str, path_file: str, users: list[str], fieldnames: str):
    
    with open(f'{path_file}/{file_name}', 'a') as txtfile:
        
        for i in range(len(users)):
            if i == 0:
                txtfile.writelines(f'{fieldnames}\n')
            txtfile.writelines(users[i] + '\n')


