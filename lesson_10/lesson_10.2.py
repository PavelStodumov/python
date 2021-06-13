class Clothes:
    def __init__(self, size=None, height=None):
        self.size = size
        self.height = height


class Coat(Clothes):
    def global_fabric(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def global_fabric(self):
        return self.height * 2 + 0.3


my_coat = Coat(size=50)  # Непонятно, какой размер указывать для пальто(многовато получается по формуле)
my_suit = Suit(height=1.78)

print(my_coat.global_fabric())
print(my_suit.global_fabric)