class Zerro_div(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise Zerro_div('Деление на ноль!!!')
except Zerro_div as ex:
    print(ex)
else:
    print(f'Частное равно: {a / b}')
