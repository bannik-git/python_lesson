import csv


def adding_data_to_the_database(user: list):
    with open('Homework/Seminar_7/base.csv', 'a', newline='') as csvfile:
        name_dict_writer = csv.DictWriter(csvfile, fieldnames=['id', 'Имя', 'Фамилия'], delimiter=';', dialect='excel-tab')
        name_dict_writer.writeheader()
        for i in user:
            name_dict_writer.writerow(i)


def print_user(user_id: str):
    with open ('Homework/Seminar_7/base.csv', 'r') as csvfile:
        name_reader = csv.DictReader(csvfile, delimiter=";")
        for i in name_reader:
            if i['id'] == user_id:
                print(i)


def delete_user(user_id: str):
    user_ditc = {}
    with open ('Homework/Seminar_7/base.csv', 'r') as csvfile:
        name_reader = csv.DictReader(csvfile, delimiter=";")
        for i in name_reader:
            if i['id'] != user_id:
                user_ditc[i['id']] = i
    print(user_ditc)                
    # with open('Homework/Seminar_7/base.csv', 'w', newline='') as csvfile:
    #     name_dict_writer = csv.DictWriter(csvfile, fieldnames=['id', 'Имя', 'Фамилия'], delimiter=';', dialect='excel-tab')
    #     name_dict_writer.writeheader()
    #     for i in user_ditc:
    #         name_dict_writer.writerow(i)