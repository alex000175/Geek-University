# 5 Канцелярская принадлежность

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки')

class Pencil (Stationery):
    def draw(self):
        print('Запуск отрисовки карандаша')

class Handle (Stationery):
    def draw(self):
        print('Запуск отрисовки маркера')

a = Stationery('Anyone')
pen = Pen('Pilot')
pencil = Pencil('Grifil')
handle = Handle('Brauberg')

a.draw()
pen.draw()
pencil.draw()
handle.draw()
