def type_logger(func):
    def wrap(*args):
        print(*(f'{func.__name__}({i}: {type(i)})' for i in args), sep=',')
        return func(*args)

    print(f'тип значения функции: {type(wrap())}')
    return wrap


@type_logger
def calc_cube(*x):
    return [i ** 3 for i in x]


a = calc_cube(5, 6, 7.3)
print(a)