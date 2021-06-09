class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Это ручка')


class Pencil(Stationery):
    def draw(self):
        print('Это карандаш')


class Handle(Stationery):
    def draw(self):
        print('Это маркер')

pen = Pen('parker')
pencil = Pencil()
handle = Handle()

pen.draw()
print(pen.title)
pencil.draw()
handle.draw()