# Написать функцию, которая производит поиск и выводит на экран вакансии 
# с заработной платой больше введённой суммы 
# (необходимо анализировать оба поля зарплаты, то есть цифра вводится одна, 
# а запрос проверяет оба поля)

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['hh']  # hh - database
vacations = db.vacations  # vacations - collection

def find_salary(min_salary):
    expensive_vacs = vacations.find({'$or': [{'payment_min':{'$gte':min_salary}}, {'payment_max':{'$gte':min_salary}}]}).sort('payment_min')

    print('Вакансии с зарплатой выше чем ', min_salary)
    for item in expensive_vacs:
        pprint(item)

# find_salary(100000)
find_salary(int(input('Введите минимальную сумму дохода:')))
