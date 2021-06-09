class Worker:
    def __init__(self, name, surname, position, *income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income[0], 'bonus': income[1]}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
        return f'{self.name} {self.surname}'

    def get_total_incom(self):
        print(self._income['wage'] + self._income['bonus'])
        return self._income['wage'] + self._income['bonus']


vasya = Position('Vasiliy', 'Pupkin', 'programmer', 15000, 1500)
vasya.get_full_name()
vasya.get_total_incom()
print(vasya.name)

vanya = Position('Ivan', 'Ivanov', 'director', 20000, 5000)
vanya.get_full_name()
vanya.get_total_incom()
print(vanya.surname)