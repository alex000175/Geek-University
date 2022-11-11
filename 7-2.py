# 2

from abc import ABC

class Clothes(ABC):
    def __init__(self, name):
        self.name = name
    def expenditure(self):
        pass


class Coat(Clothes): # пальто
    def __init__(self, name, size):
        self.size = size
        Clothes.name = name
    @property
    def expenditure(self):
        return round((self.size / 6.5 + 0.5), 2)

class Suit(Clothes): # костюм
    def __init__(self, name, height):
        self.height = height
        Clothes.name = name

    @property
    def expenditure(self):
        return 2 * self.height+ 0.3

a = Coat('пальто', 48)
b = Suit('костюм', 175)

print(f'расход ткани на пальто {a.expenditure}')
print(f'расход ткани на костюм {b.expenditure}')
print(f'Суммарный расход ткани {a.expenditure} + {b.expenditure} = {a.expenditure + b.expenditure}')