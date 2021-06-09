class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def global_asphalt_weight(self, depth=5):
        '''По умолчанию метод расчитывает общую массу асфальта для покрытия тощиной 5 см.
        Толщину можно передать аргументом в метод'''
        __weight = 25
        print(f'{self._length * self._width * __weight * depth // 1000} тонн')


e95 = Road(5000, 20)
e95.global_asphalt_weight()
e95.global_asphalt_weight(10)

