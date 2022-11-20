# 1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»

import calendar

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def date_to_int(cls, data):
        return int(data.replace('.',''))

    @classmethod
    def day_to_int(cls, data):
        return int(data.split('.')[0])

    @classmethod
    def month_to_int(cls, data):
        return int(data.split('.')[1])

    @classmethod
    def yearh_to_int(cls, data):
        return int(data.split('.')[2])

    @staticmethod
    def ch_to_date(data):
        if len(data) > 10 or len(data) < 9 or data.count('.') != 2:
            return 'Ошибка формата данных! Введите дату в формате dd.mm.yyyy'
        d = int(data.split('.')[0])
        m = int(data.split('.')[1])
        y = int(data.split('.')[2])
        mm = '135'
        if 1900 < y > 2022:
            return 'Ошибка даты! Укажите год с 1900 по 2022'

        if 1 < m > 12:
            return 'Ошибка даты! Укажите месяц от 1 до 12'

        if 1 < d > calendar.monthrange(y, m)[1]:
            return 'Ошибка даты! Для ' + str(m) + '-го месяца укажите день от 1 до ' + str(calendar.monthrange(y, m)[1])

        return 'дата указана верно'


new_date = Data('17.11.2022')



print(Data.date_to_int('17.11.2022'))

print(Data.day_to_int('17.11.2022'))
print(Data.month_to_int('17.11.2022'))
print(Data.yearh_to_int('17.11.2022'))

print(Data.ch_to_date('32.11.2022'))
