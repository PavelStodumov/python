tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б']


# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

def get_tutors_klasses(list_1, list_2):
    if len(list_1) > len(list_2):
        list_2.extend(None for i in range(len(list_1) - len(list_2)))
    for i in range(len(list_1)):
        yield (list_1[i], list_2[i])


# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:

bouth = get_tutors_klasses(tutors, klasses)

# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
try:
    print(type(bouth))
    for i in bouth:
        print(i)
    print(next(bouth))
except StopIteration:
    print('генератор истощен')
