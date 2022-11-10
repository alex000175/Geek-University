# 2. Расчет массы асфальта для дороги

class Road():
    _length = 0
    _width = 0
    higt = 5
    massa = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        try:
            print(f'{self._length * self._width * self.higt * self.massa / 1000} т.')
        except TypeError:
            print('Введите цифровое значение параметра!')
        except:
            print('Ошибка выполнения метода!')

a = Road(20, 5000)
# a.higt = 5  # высота дорожного плотна
# a.massa = 25 # масса асфальта на площади 1 кв метр
a.calc()