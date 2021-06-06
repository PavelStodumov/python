def val_checker(f):
    def _val_checker(func):
        def wrap(arg):
            if f(arg):
                return func(arg)
            else:
                raise ValueError(f'wrong val {arg}')
        return wrap
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
