# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a > b:
            n1  = a if a > c else c
            return n1 + a
        else:
            n1 = b if b > c else c
            return n1 + b
    except:
        return "Функция принимает только числовые значения!"



print(my_func(input("Введите первое число:"),input("Введите второе число:"),input("Введите третье число:")))