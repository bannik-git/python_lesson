import controller

dict_fieldnames = {1:'Имя', 2:'Фамилия', 3:'Телефон', 4:'Примечание'}
fieldnames = ['id', 'Имя', 'Фамилия', 'Телефон', 'Примечание']

path = 'Homework/Seminar_7/base.csv'
controller.work(path, dict_fieldnames, fieldnames)
