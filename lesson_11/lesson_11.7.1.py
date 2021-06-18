import re

class Complex:
    def __init__(self, view):
        self.view = view
        if ' ' in view:
            self.a = ''.join(view.split(' ')[:-2])
        else:
            self.a = 0
        self.b = ''.join(view.split(' ')[-2:])

    def __str__(self):
        return self.view

    def __add__(self, other):

        a = str(int(self.a) + int(other.a))
        if (self.b[:-1].isdigit() or self.b[1:-1].isdigit()) and (other.b[:-1].isdigit() or other.b[1:-1].isdigit()):
            b = str(int(self.b[:-1]) + int(other.b[:-1]))
        elif not self.b[:-1].isdigit():
            b = other.b[:-1]
        elif not other.b[:-1].isdigit():
            b = self.b[:-1]


        if b.startswith('-'):
            return Complex(f'{a} - {b[1:]}i')
        else:
            return Complex(f'{a} + {b}i')
    def __mul__(self, other):
        a = str(int(self.a) * int(other.a) + int(self.b[:-1]) * int(other.b[:-1]) * -1)
        b = str(int(self.a) * int(other.b[:-1]) + int(self.b[:-1]) * int(other.a))
        if b.startswith('-'):
            return Complex(f'{a} - {b[1:]}i')
        else:
            return Complex(f'{a} + {b}i')


num1 = Complex('3 + 1i')
num2 = Complex('5 - 2i')

print(num1 + num2)
print(num1 * num2)
'''Работает кривовато, в числах где b == 1 нужно это явно указывать '''