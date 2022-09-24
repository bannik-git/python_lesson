def compress_string(user_string: str) -> str:
    'Сжимает строку из вида "aaafffrrrddee" в "a3f3r3d2e2"'
    char = str_base[0]
    count = 1
    result = ''
    for i in range(1, len(str_base)):
        if char == str_base[i]:
            count += 1
        else:
            result += f'{char}{count}'
            char = str_base[i]
            count = 1
            
    result += f'{char}{count}'
    return result


def data_extraction(compress_string: str) -> str:
    'Перевод строки из сжатого(a3f3r3d2e2) в нормальное состояние(aaafffrrrddee)'
    result = ''
    for i in range(0, len(compress_string), 2):
        result += compress_string[i] * int(compress_string[i + 1])
    return result


str_base = 'aaaaffffrrrdddeeetttyyy'
result_compress = compress_string(str_base)
print(result_compress)

extraction_str = data_extraction(result_compress)
print(extraction_str)
