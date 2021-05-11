duration = input()
while duration.isdigit():
    duration = int(duration)
    days = duration // 86400
    print('duration =', duration)
    if days:
        print(f'{days} дн', end=' ')
    hours = duration % 86400 // 3600
    if hours:
        print(f'{hours} час', end=' ')
    minutes = duration % 86400 % 3600 // 60
    if minutes:
        print(f'{minutes} мин', end=' ')
    seconds = duration % 86400 % 3600 % 60
    if seconds:
        print(f'{seconds} сек')
    duration = input()
# Постарался сделать "вывод" максимально похожий с методичкой.
