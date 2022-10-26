# 6
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран
from pprint import pprint

try:
    f = open('readme6.txt', 'r', encoding='utf-8')
    st = {}
    for line in f:
        sum = 0
        for j in list(line.split(':')[1].split(' ')):
            s = ''
            for lette in range(len(j)):
                if j[lette].isdigit():
                    s += j[lette]
            if len(s) > 0:
                sum += int(s)
        st[list(line.split(':'))[0]] = sum
    f.close()
    pprint(st)
except IOError:
    print("An IOError has occurred!")
finally:
    f.close()
