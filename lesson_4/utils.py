import sys
import currency

try:
    if sys.argv[1] == 'info':
        currency.valute_list()
    else:
        if currency.currency_rates(sys.argv[1]) == None:  # не понимаю, почему подчеркнуто
            print('Такой валюты нет в нашем списке. <info> для информации')
except IndexError:
    print("Введите код валюты для конвертации в рубли или <info> для информации")

# старался. Хочется сделать достойно разбора на уроке))
