from Password import Password
import datetime
import os
from rich import print, box
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text


def file_name():
    text_datetime = f'{datetime.datetime.now()}'
    symbols_replace = ['-', ' ', ':', '.']
    fn = ''
    for s in text_datetime:
        is_write = True
        for sr in symbols_replace:
            if s == sr:
                fn += '_'
                is_write = False
        if is_write:
            fn += s
    return fn


password = Password()

count_symbols = input("Введите количество символов в пароле: ")

if count_symbols.isdigit():
    password.generation(int(count_symbols))
else:
    password.generation(None)

# print(f'Версия рограммы: v0.0.4')
# print(f'Доступные символы: {password.get_array_symbols()}')
# print(f'Количество доступных символов: {len(password.get_array_symbols())}')
# print(f'Количество возможных комбинаций: {password.count_variant}')
#
# print(f'Сгенерированный пароль: {password}')

layout = Layout(name="info")

print_count_array_symbols = Text.form_markup(
    f'Количество доступных символов: {len(password.get_array_symbols())}',
    style="bold yellow"
)

print_array_symbols = Text.form_markup(
    f'Доступные символы: {password.get_array_symbols()}',
    style="bold yellow"
)

print_count_variant = Text.form_markup(
    f'Количество возможных комбинаций: {password.count_variant}',
    style="italic #af00ff"
)

print_password = Text.form_markup(
    f'Сгенерированный пароль: {password.password}',
    style="bold yellow"
)


console = Console()
layout = Layout(name="info")

layout.update(
    Panel(
        Group(
            print_count_array_symbols,
            print_array_symbols,
            print_count_variant,
            print_password,
        ),
        box=box.ROUNDED,
        title="Информация",
        subtitle="Версия рограммы: v0.0.4",
    )
)

console.print(layout)

if not os.path.exists('passwords'):
    os.mkdir('passwords')

# Запись пароля в файл
with open(f'password/{file_name}_password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))

input()
