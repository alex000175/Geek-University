# итератор, генерирующий целые числа, начиная с указанного;

n = int(input('Введите целое число от 0 до 9: '))
# n = 2
def numbers_range(x):
    while True:
        x = x + 1
        if x > 10:
            break
        yield (x)

a = numbers_range(int(n))
for i in a:
    print(i)

# итератор, повторяющий элементы некоторого списка, определённого заранее
# -----------------------------------------------------------------------
from itertools import cycle

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
iterator = cycle(my_list)

x = 0
for i in iterator:
    print(i)
    x += 1
    if x > 10:
        break