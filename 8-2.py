# 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите положительное число: ")
inp_data2 = input("Введите положительное число: ")
try:
    a = int(inp_data)
    b = int(inp_data2)
    if a < 0 or b < 0:
        raise OwnError("Ошибка: Вы ввели отрицательное число!")

    if b == 0:
        raise OwnError("Ошибка: Делитель не может равняться 0")
    c = a/b

except OwnError as err:
    print(err)
except (ValueError, OwnError) as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {c}")