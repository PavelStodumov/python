# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
def num_translate(numb):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if numb.istitle():
        return num_dict.get(numb.lower()).capitalize()
    else:
        return num_dict.get(numb.lower())


print(num_translate('Five'))
print(num_translate('six'))
print(num_translate('eleven'))
