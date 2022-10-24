# итератор, генерирующий целые числа, начиная с указанного;

from sys import argv
name, n = argv
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
