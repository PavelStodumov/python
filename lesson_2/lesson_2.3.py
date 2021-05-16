# Дан список:
get_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
print(get_list, id(get_list))

ind = 0
while ind < len(get_list[:]):            # решил использовать такой цикл, так как список будет расширяться
    new_elem = ''                        # через for были ошибки 'index out of range'
    new_elem_num = ''
    for symbol in get_list[ind]:         # большая часть кода из предыдущей задачи
        if symbol.isdigit():
            new_elem_num += symbol
        else:
            new_elem += symbol
    if new_elem_num:
        new_elem += new_elem_num.zfill(2)
        get_list[ind] = '"'
        get_list.insert(ind, new_elem)
        get_list.insert(ind, '"')
        ind += 4
    else:
        get_list[ind] = new_elem
        ind += 1

my_string = ' '.join(get_list)  # в пулученной строке пробелы внутри кавычек
my_new_string = ''

for symbol in my_string:  # удаляем пробелы внутри кавычек
    if symbol == ' ':
        if my_new_string[-1] == '"' and my_new_string.count('"') % 2:
            continue
        elif my_new_string.count('"') % 2:
            continue
    my_new_string += symbol

print(get_list, id(get_list))
print(my_new_string)

# было не просто

