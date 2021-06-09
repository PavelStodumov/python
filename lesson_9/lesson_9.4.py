class Car:
    def __init__(self, speed, color, name, turn='d', is_police=False):
        '''По умолчанию машина едет прямо, для поворота turn ввести 'l' или 'r'.'''
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.turn = turn

    def go(self):
        if self.speed > 0:
            print('Машина поехала')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn_direction(self):
        if self.turn == 'l':
            print('Машина поворачивает на лево')
        elif self.turn == 'r':
            print('Машина поворачивает на право')
        else:
            print('Машина двигается прямо')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')


class SportCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed < 100:
            print('Принижение скорости!')


class PoliceCar(Car):
    pass


prius = TownCar(60, 'white', 'Toyota', 'l')
transporter = WorkCar(55, 'grey', 'VolksWagen', 'r')
camaro = SportCar(90, 'yellow', 'Chevrolet')
samara = PoliceCar(0, 'white', 'Lada', is_police=True)

prius.show_speed()
prius.turn_direction()

transporter.show_speed()
transporter.turn_direction()

camaro.show_speed()
camaro.turn_direction()
print(camaro.__dict__)
