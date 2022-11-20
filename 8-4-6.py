# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
import datetime


class Sklad:
    def __init__(self, name, adress, manager, date='01.01.2000'):
        self.name = name
        self.adress = adress
        self.manager = manager
        self.date = str(datetime.datetime.now())

    def __str__(self):
        return '---- информация о складе---- \n'  \
               'Название: ' + self.name + '\n'  \
                'Адрес: ' + self.adress +'\n' \
                'Управляющий: ' + self.manager + '\n' \
                'Дата открытия: ' + self.date


    @property
    def info(self):
        return self.name + '(' + self.adress +')'

class Equipment:
    def __init__(self, sklad, manufacturer, model, price, count=0, date_income='01.01.2022'):

        try:
            self.sklad = sklad
            self.manufacturer = str(manufacturer)
            self.model = str(model)
            self.price = float(price)
            self.date_income = datetime.datetime.now()
            self.count = int(count)
        except:
            print('Ошибка преобразования данных. Введите корректные данные!')


    db = {}

    @property
    def info(self):
        tr = Equipment.db[self.manufacturer + ' ' + self.model]
        nl = ''
        for i in range(len(tr)):
            nl += str(tr[i]) + '\n'

        return 'Транзакции по оборудованию ' + self.manufacturer + ' ' + self.model + '\n' + nl

    def add(self, count):
        try:
            self.count += count
            Equipment.db[self.manufacturer + ' ' + self.model].append(list([str(self.date_income)[:16], 'income', count, self.count]))
        except:
            print('Вы ввели некорректные данные!')

    def sale(self, count):
        try:
            self.count -= count
            Equipment.db[self.manufacturer + ' ' + self.model].append(list([str(self.date_income)[:16], 'sale', count, self.count]))
        except:
            print('Вы ввели некорректные данные!')

class Printer(Equipment):
    def __init__(self, sklad, manufacturer, model, price, count=0, A4=True, color=False, date_income='01.01.2022'):
        super().__init__(sklad, manufacturer, model, price, count, date_income)
        self.A4 = A4
        self.color = color
        Equipment.db[self.manufacturer + ' ' + self.model] = [['Дата транзакции','Тип','Кол-во','Остаток']]

    def __str__(self):
        return '---- информация о товаре---- \n'  \
               'Группа товара: Принтеры \n'  \
                'Производитель: ' + self.manufacturer +'\n' \
                'Модель: ' + self.model +'\n' \
                'Формат А4: ' + str(self.A4) +'\n' \
                'Цветная печать: '  + str(self.color) +'\n' \
                'Цена: ' + str(self.price) + '\n' \
                'Остаток: ' + str(self.count)




class Scaner(Equipment):
    def __init__(self, sklad, manufacturer, model, price, count=0, MFU = False, date_income='01.01.2022'):
        super().__init__(sklad, manufacturer, model, price, count, date_income)
        self.MFU = MFU
        Equipment.db[self.manufacturer + ' ' + self.model] = [['Дата транзакции', 'Тип', 'Кол-во', 'Остаток']]


    def __str__(self):
        return '---- информация о товаре---- \n'  \
               'Группа товара: Сканеры\n'  \
                'Производитель: ' + self.manufacturer +'\n' \
                'Модель: ' + self.model +'\n' \
                'МФУ: ' + str(self.MFU) + '\n' \
                'Цена: ' + str(self.price) + '\n' \
                'Остаток: ' + str(self.count)



# --------------------------------------------------------------------
MyS = Sklad('Склад оргтехники', 'г. Москва', 'Иванов И.И.')
# print(MyS)

Epson240 = Printer(MyS, 'Epson','E240','5400')
Epson240.add(7)
Epson240.add(5)
Epson240.add(3)
Epson240.sale(1)
Epson240.sale(4)

Canon1156 = Printer(MyS, 'Canon','1156',6000)
Canon1156.add(1)
Canon1156.add(2)
Canon1156.add(3)
Canon1156.sale(2)


print(Epson240.info)

print(Canon1156.info)