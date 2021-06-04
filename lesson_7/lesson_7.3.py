import os
import shutil


class DirAlredyCopying(Exception):
    pass


root_dir = 'my_project'
try:
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                rel_path = os.path.join(root, file)
                new_path = os.path.join(root_dir, '\\'.join(rel_path.split('\\')[2:-1]))
                if (os.path.exists(os.path.join(new_path, os.path.split(rel_path)[-1]))):
                    raise DirAlredyCopying
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                    shutil.copy(rel_path, new_path)
                else:
                    shutil.copy(rel_path, new_path)
except DirAlredyCopying:
    print('Файлы скопированы')
# Вроде получилось, но было очень не просто
