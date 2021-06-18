class Warhouse:
    war_val = {}

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Свободных мест {self.value}'

    def fill(self, name, value):
        try:
            if self.value - value < 0:
                print('Склад переполнен')
            else:
                self.value -= value
                if str(name) in self.war_val:
                    self.war_val[str(name)] += int(value)
                else:
                    self.war_val[str(name)] = int(value)
        except TypeError:
            print('Используйте числа для ввода количества')

    def take(self, name, value):
        try:
            if str(name) not in self.war_val:
                print(f'Товара {name} нет на складе')
            else:
                if self.war_val[str(name)] - value > 0:
                    self.war_val[str(name)] -= value
                    self.value += value
                else:
                    print(f'Недостаточное количество {name} на складе')
        except TypeError:
            print('Используйте числа для ввода количества')


''' При создании объекта склада указывается его вместимость. Для пополнения или выгрузки в качестве аргументов передаются
наименование и количество в числовом виде. Учитывается наличие свободного места при пополнении, а так же наличие товара 
и его количество при выгрузке'''


class Office_equipment:
    def __init__(self, brand):
        self.brand = brand


class Printer(Office_equipment):
    def __init__(self, brand, model):
        self.model = model
        super().__init__(brand=brand)

    def __str__(self):
        return self.brand + self.model


class Xerox(Office_equipment):
    def __init__(self, brand, model):
        super().__init__(brand=brand)
        self.model = model

    def __str__(self):
        return self.brand + self.model


class Scaner(Office_equipment):
    def __init__(self, brand, model):
        Office_equipment.__init__(self, brand=brand)
        self.model = model

    def __str__(self):
        return self.brand + self.model


dell5334 = Scaner('dell', '5334')
hp1234 = Xerox('hp', '1234')

my_warhouse = Warhouse(1000)
my_warhouse.fill(hp1234, 20)
my_warhouse.fill(dell5334, 30)

print(my_warhouse.war_val)
print(my_warhouse)

my_warhouse.take(dell5334, 40)
my_warhouse.take(hp1234, 10)

print(my_warhouse.war_val)
print(my_warhouse)
