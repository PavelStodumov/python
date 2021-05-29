import sys

try:

    # print('Введите имя файла с пользователями: ')
    with open(sys.argv[1], 'r', encoding='utf-8') as f_u:

        users = (user for user in f_u.read().strip().split('\n'))
        users_hobbys = {user: None for user in users}

        # print('Введите имя файла с хобби пользователей: ')
        with open(sys.argv[2], 'r', encoding='utf-8') as f_h:
            hobbys = (hobby for hobby in f_h.read().strip().split('\n'))
            users_hobbys.update({user: hobby for user, hobby in zip(users_hobbys.keys(), hobbys)})

    # print('Введите имя конечного файла с именами: хобби: ')
    with open(sys.argv[3], 'w+', encoding='utf-8') as f:
        for user, hobby in users_hobbys.items():
            f.write(f'{user}: {hobby}\n')
        print(users_hobbys)
        print('записано в файл')

    if len(list(hobbys)):
        print('Код 1. Увлечений бельше чем пользователей')
except:
    print('Неверное имя файла')

exit()
