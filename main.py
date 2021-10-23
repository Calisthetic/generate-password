import random
import datetime
import os

# Набор доступных символов
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '.', ',',
    '=', '|', '/', '<', '>', ';', ':', '`', '~', '{', '}', '[', ']', '?', "'"
]
# Получаем количество символов в пароле
input_count = input('Введите количество символов в пароле: ')
if input_count.isdigit():
    count_symbols = int(input_count)
else:
    count_symbols = 8
    print('Вы ввели строку, требуется число')

# Считаем количество возможных комбинаций
count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Получить случайный символ
def random_symbols():
    return ARRAY_SYMBOLS[random.randint(0, len(ARRAY_SYMBOLS) - 1)]


print(f'Версия рограммы: v0.0.2')
print(f'Доступные символы: {ARRAY_SYMBOLS}')
print(f'Количество доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Количество возможных комбинаций: {count_variant}')

# Генерируем пароль
password = ''
for i in range(0, count_symbols):
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

text_datetime = f'{datetime.datetime.now()}'
symbols_replace = ['-', ' ', ':', '.']
file_name = ''
for s in text_datetime:
    is_write = True
    for sr in symbols_replace:
        if s == sr:
            file_name += '_'
            is_write = False
    if is_write:
        file_name += s

if not os.path.exists('passwords'):
    os.mkdir('passwords')

#
with open(f'password/{file_name}_password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))

input()

