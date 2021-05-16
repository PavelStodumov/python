# Дан список:
get_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
get_new_list = []

for elem in get_list:               # перечисляем список поэлементно
    new_elem = ''
    new_elem_num = ''
    for symbol in elem:             # каждый элемент перечисляем посимвольно
        if symbol.isdigit():
            new_elem_num += symbol
        else:
            new_elem += symbol
    if new_elem_num:
        get_new_list.append('"')
        new_elem += new_elem_num.zfill(2)       # если новый элемент-число, увеличиваем его длинну до двух
        get_new_list.append(new_elem)
        get_new_list.append('"')
    else:
        get_new_list.append(new_elem)
print(get_list)
print(get_new_list)
my_string = ' '.join(get_new_list)              # в пулученной строке пробелы внутри кавычек
print(my_string)

my_new_string = ''

for symbol in my_string:                         # удаляем пробелы внутри кавычек
    if symbol == ' ':
        if my_new_string[-1] == '"' and my_new_string.count('"') % 2:
            continue
        elif my_new_string.count('"') % 2:
            continue
    my_new_string += symbol
print(my_new_string)




