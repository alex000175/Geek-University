# 3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
try:
    f = open('readme3.txt', 'r', encoding='utf-8')
    st = []
    sum = 0
    i = 0
    all_sum = 0
    for line in f:
        if len(line) > 2:
            i += 1
            sum = float(line.split(' ')[1])
            all_sum += sum
            if sum < 20000:
                st.append(line.split(' ')[0])
                # st[line.split(' ')[0]] = float(line.split(' ')[1])
    f.close()
    pprint(st)
    print(f'Средняя ЗП всех сотрудников: {all_sum / i:.2f}')
except IOError:
    print("An IOError has occurred!")
finally:
    f.close()
