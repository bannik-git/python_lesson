from prettytable import PrettyTable

def data_request(text: str) -> str:
    return input(text)

def print_user(users: list[dict], fieldnames: list):
    string = PrettyTable()
    string.field_names = fieldnames

    for i in users:
        result_str = ''
        for k in i.values():
            result_str += f'{k} '   
        string.add_row(list(result_str.split()))
    
    print(string)

