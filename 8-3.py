# 3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

sp = []
print ('Введите числа для заполнения списка. Для остановки скрипта введите stop')

while True:
    inp_data = input("Введите число: ").replace(",",".")
    if inp_data.lower() == 'stop':
        print(sp)
        break
    try:
        if inp_data.count('.') == 1:
            nn = float(inp_data)
        else:
            nn = int(inp_data)
    except (ValueError, OwnError) as err:
        print(err)
        # break
    else:
        sp.append(nn)
        print(f"Число {nn} добавлено в список")
        print('------------------------------')
