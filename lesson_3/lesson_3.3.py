# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*args):
    get_dict = {}
    for elem in args:
        if elem[0] not in get_dict:
            get_dict.update({elem[0]: [elem]})
        else:
            get_dict[elem[0]] += [elem]
    return get_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
