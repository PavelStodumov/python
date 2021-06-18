class Is_num(Exception):
    def __init__(self, text):
        self.text = text


is_list = []
while True:
    try:
        elem = input('Введите число для пополнения списка\nили ничего не вводите чтобы остановить: ')
        if elem:
            if elem.isdigit():
                is_list.append(int(elem))
            else:
                raise Is_num('введено не число')
        else:
            break
    except Is_num as e:
        print(e)

print(is_list)
