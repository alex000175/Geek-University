# 4. Базовый класс Car

class Car:

    def __init__(self, name, color, is_police, speed):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print('Поехали!!!')
        if self.speed == 0:
            self.speed += 10

    def stop(self):
        print('Остановились')
        print('----------------------------')
        self.speed = 0

    def turn(self, direction):
        if direction == 'left':
            print('Повернули налево')
        elif direction == 'right':
            print('Повернули направо')
        else:
            print('Не знаю такое направлене, еду дальше!')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def go(self):
        print('Town car: Поехали!!!')
        if self.speed == 0:
            self.speed += 10

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость превышает {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed} км/ч')

class WorkCar(Car):
    def go(self):
        print('Work car: Поехали!!!')
        if self.speed == 0:
            self.speed += 10

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость превышает {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed} км/ч')

class PoliceCar(Car):
    def go(self):
        print('Police car: Поехали!!!')
        if self.speed == 0:
            self.speed += 10

class SportCar(Car):
    def go(self):
        print('Sport car: Поехали!!!')
        if self.speed == 0:
            self.speed += 10

a = Car('mustang', 'red', False, 0)
a.go()
a.turn('left')
a.show_speed()
a.stop()

b = TownCar('Wolkswagen', 'blue', False, 65)
b.go()
b.show_speed()
b.stop()

c = PoliceCar('Chevrolet', 'yellow', True, 120)
c.go()
c.turn('right')
c.turn('left')
c.show_speed()
c.stop()

d = SportCar('Ferrary', 'red', True, 220)
d.go()
d.turn('right')
d.turn('left')
d.show_speed()
d.stop()