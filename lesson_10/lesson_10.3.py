class Cell:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return Cell(self.value + other.value)

    def __sub__(self, other):
        return self.value - other.value if self.value - other.value > 0 else 'Нельзя вычесть'

    def __mul__(self, other):
        return self.value * other.value
    def __floordiv__(self, other):
        return self.value // other.value if self.value > other.value else other.value // self.value

    def make_order(self, num):
        self.num = num
        return '\n'.join(['*' * num for _ in range(self.value // num)] + [self.value % num * '*'])


cell_1 = Cell(50)
cell_2 = Cell(60)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(15))