import os

dict_dirs = {'my_project': [
    {'authapp': [
        '__init__.py', 'models.py', 'views.py',
        {'templates': [
            {'authapp': [
                'base.html', 'index.html']}]}]},
    {'mainapp': [
        'views.py', 'models.py', '__init__.py',
        {'templates': [
            {'mainapp': [
                'base.html', 'index.html']}]}]},
    {'settings': [
        '__init__.py', 'dev.py', 'prod.py']}]}
'''
Не знаю, насколько оптимально хранить конфигурацию в словаре...
посмотрев запись урока, понял что структуру файла можно было самому переписать.
очень много времени потратил, чтобы файл из примера преобразовать в мой словарь. Так и не смог
может позже вернусь
'''



def create_starter(dict):
    for key, value in dict.items():
        if not os.path.exists(key):
            os.mkdir(key)
            os.chdir(key)
        else:
            os.chdir(key)
        for val in value:
            if '.' in val:
                with open(val, 'w', encoding='utf-8') as f:
                    pass
            else:
                create_starter(val)
        os.chdir('..')
# Никогда не понимал рекурсию...


create_starter(dict_dirs)
