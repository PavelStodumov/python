# import random
#
# get_list = [round(random.uniform(1, 100), 2) for i in range(20)]
from copy import deepcopy

# Создать вручную список, содержащий цены на товары (10–20 товаров) (такое себе удовольствие =))
get_list = [38.3, 4, 40.07, 58.19, 43.54,
            89.92, 46.89, 8.31, 58.6, 92.47,
            64.25, 22.82, 34.39, 35.32, 16.38,
            9.58, 34.4, 74.62, 63.58, 47.31]
print(get_list)
print(id(get_list))

for elem in get_list:
    get_list[get_list.index(elem)] = str(elem).split('.')

for elem in get_list:
    elem[0] += ' руб'
    if len(elem) > 1:
        elem[1] = f'{elem[1]:0<2} коп'
    else:
        elem.append('00 коп')


def printer_list(some_list):  # напечатать хотелось без запятой в конце(красиво)
    for ind in range(len(some_list)):
        if ind == len(some_list) - 1:
            print(' '.join(some_list[ind]))
        else:
            print(' '.join(some_list[ind]), end=', ')


def value(some_list):  # вычисляем числовое значение для сортировки по ключу
    num = ''
    for el in '.'.join(some_list):
        if el.isdigit() or el == '.':
            num += el
    return float(num)


# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
printer_list(get_list)
print(id(get_list))

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
get_list.sort(key=value)
printer_list(get_list)
print(id(get_list))

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
get_list_new = sorted(get_list, key=value, reverse=True)
printer_list(get_list_new)
print(id(get_list_new))

# Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
printer_list(get_list_new[:5])
printer_list(sorted(get_list, key=value, reverse=True)[:5])
