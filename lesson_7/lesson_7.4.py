import os
import json


def folder_summary(folder):
    files_stat = {100: 0, 1000: 0, 10000: 0, 100000: 0}
    ext_dict = {100: set(), 1000: set(), 10000: set(), 100000: set()}
    for roots, dirs, files in os.walk(folder):
        for file in files:
            if os.path.getsize(os.path.join(roots, file)) < 100:
                files_stat[100] += 1
                ext_dict[100].add(file.split('.')[-1])
            elif 100 <= os.path.getsize(os.path.join(roots, file)) < 1000:
                files_stat[1000] += 1
                ext_dict[1000].add(file.split('.')[-1])
            elif 1000 <= os.path.getsize(os.path.join(roots, file)) < 10000:
                files_stat[10000] += 1
                ext_dict[10000].add(file.split('.')[-1])
            else:
                files_stat[100000] += 1
                ext_dict[100000].add(file.split('.')[-1])
    for key, value in files_stat.items():
        files_stat[key] = (files_stat[key], list(ext_dict[key]))
    with open(f'{os.path.split(folder)[-1]}_summary.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(files_stat))


folder_summary('my_project')
