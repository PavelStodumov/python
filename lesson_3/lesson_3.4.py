# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.

def thesaurus(*args):
    get_dict = {}
    for elem in args:
        if elem[0] not in get_dict:
            get_dict.update({elem[0]: [elem]})
        else:
            get_dict[elem[0]] += [elem]
    return get_dict


def thesaurus_adv(*args):
    get_dict = {}
    for elem in args:

        if elem[elem.find(' ') + 1] not in get_dict:
            get_dict[elem[elem.find(' ') + 1]] = thesaurus(elem)
        else:
            if elem[0] in get_dict[elem[elem.find(' ') + 1]]:
                get_dict[elem[elem.find(' ') + 1]][elem[0]] += [elem]
            else:
                get_dict[elem[elem.find(' ') + 1]].update(thesaurus(elem))
    return get_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

# во я нагородил то. не удивлюсь если можно в пару строчек решить
# зато работает
