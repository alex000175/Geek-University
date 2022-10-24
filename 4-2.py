# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор

from random import sample

# my_list = sample(range(1, 101), 20)
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

def numbers_range(my_list):
    for i in range(len(my_list)):
        if my_list[i - 1] < my_list[i]:
            yield my_list[i]

a = numbers_range(my_list)

for i in a:
    new_list.append(i)

print(new_list)