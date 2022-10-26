# 7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

from pprint import pprint
import json

try:
    f = open('readme7.txt', 'r', encoding='utf-8')
    my_list = []
    sr_prib = 0
    j = 0
    st = {}
    st2 = {}
    for line in f:
        tip = line.split(' ')[1]
        name = line.split(' ')[0]
        v = float(line.split(' ')[2])
        iz = float(line.split(' ')[3])
        prib = v - iz
        if prib > 0:
            sr_prib += prib
            j += 1
        st[name] = prib

    st2['average_profit'] = round(sr_prib / j, 2)
    my_list.append(st)
    my_list.append(st2)
    pprint(my_list)

    with open('file_j.json', 'w', encoding='utf-8') as jf:
        json.dump(my_list, jf)
except IOError:
    print("An IOError has occurred!")
finally:
    f.close()
