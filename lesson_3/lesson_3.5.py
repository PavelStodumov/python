# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)

from random import randrange


def get_jokes(num, flag=False):
    '''
    num - количество шуток
    flag - исключение повторений слов
    если flag=True - шуток не может быть больше
    чем слов в самом коротком списке
    (на данный момент 5)
    '''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag:
        for i in range(num):
            _jokes = []
            _jokes.append(nouns.pop(randrange(0, len(nouns))))
            _jokes.append(adverbs.pop(randrange(0, len(adverbs))))
            _jokes.append(adjectives.pop(randrange(0, len(adjectives))))
            jokes.append(' '.join(_jokes))
        print(jokes)
        return jokes
    else:
        for i in range(num):
            _jokes = []
            _jokes.append(nouns[randrange(0, len(nouns))])
            _jokes.append(adverbs[randrange(0, len(adverbs))])
            _jokes.append(adjectives[randrange(0, len(adjectives))])
            jokes.append(' '.join(_jokes))
        print(jokes)
        return jokes


get_jokes(6)
get_jokes(5, True)
print(help(get_jokes))
