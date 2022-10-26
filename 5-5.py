# 5
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран
from random import randrange

f = open('readme5.txt', 'w', encoding='utf-8')
my_list = [randrange(1, 50, 1) for i in range(20)]
sum = 0
for n in my_list:
    sum += n

my_list = [str(i) for i in my_list]
f.write(" ".join(my_list))
f.close()
print(f'Сумма чисел = {sum}')
