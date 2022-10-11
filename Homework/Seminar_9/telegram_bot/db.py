
def get_token():
    with open('C:/Users/admin/Desktop/GeekBrains/Python/Token.txt', 'r') as file:
        reader = file.read().split('\n')[-1]
    return reader