# 3. Расчет заработной платы

class Worker:
    _income = {"wage": 5000, "bonus": 3000}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.position = position

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Общий доход: {sum(self._income.values())} руб.')

a = Position('Bob', 'Facker', 'manager')
a.get_full_name()
a.get_total_income()

