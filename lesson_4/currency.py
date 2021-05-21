from requests import get
import datetime


def valute_list():
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    my_list = response.split('><')
    my_list = list(filter(lambda x: 'Char' in x or 'Name' in x, my_list))
    my_list = list(map(lambda x: x[x.find('>') + 1:x.find('<')], my_list))
    for i in range(len(my_list)):
        if i % 2:
            print(f'{my_list[i - 1]}: {my_list[i]}')


def currency_rates(key):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    my_list = response.split('><')
    date_now = my_list[1].split('"')
    date_now = datetime.date(*map(lambda x: int(x), date_now[1].split('.')[::-1]))
    my_list = list(filter(lambda x: 'Char' in x or 'Value' in x, my_list))
    my_list = list(map(lambda x: x[x.find('>') + 1:x.find('<')], my_list))
    my_dict = {}
    for i in range(len(my_list)):
        if i % 2:
            my_dict.update({my_list[i - 1]: round(float(my_list[i].replace(',', '.')), 2)})
    if key.upper() in my_dict:
        print(f'{my_dict[key.upper()]},', date_now)
        return my_dict[key.upper()], date_now
    else:
        return None


if __name__ == '__main__':
    currency_rates('Eur')
    for i in currency_rates('usd'):
        print(type(i))  # по заданию типы должны быть float и data

# думаю в decimal нет смысла, так как он предназначен для большей точности при работе с
# иррациональными числами(как я понял)
