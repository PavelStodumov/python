import re


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_num(cls, param):
        return list(map(lambda x: int(x), param.date.split('-')))

    @staticmethod
    def is_valid_date(date):
        valid = re.compile(r'\d{1,2}[-]\d{1,2}[-]\d{1,4}')
        if re.findall(valid, date):
            date = list(map(lambda x: int(x), date.split('-')))
            if 0 < date[0] < 32 and 0 < date[1] < 13 and date[2] > 0:
                return True
            else:
                return False
        else:
            return False



while True:
    my_date = input('Введите дату в формате "дд-мм-гг"\nили не вводите ничего: ')
    if my_date:
        if Date.is_valid_date(my_date):
            my_date = Date(my_date)
            print('верная дата')
            print(f'Дата состоит из чисел{Date.date_to_num(my_date)}')
        else:
            print('не верная дата')
    else:
        break


