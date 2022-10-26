# 2
# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке
from pprint import pprint

try:
    f = open('readme2.txt', 'r', encoding='utf-8')
    st = {}
    i = 0
    for line in f:
        i += 1
        st[i] = 'слов: ' + str(len(list(line.split(' ')))) + '; символов: ' + str(len(line))
    f.close()
    pprint(st)
except IOError:
    print("An IOError has occurred!")
finally:
    f.close()
