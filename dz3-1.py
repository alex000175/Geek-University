# Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB 
# и реализовать функцию, которая будет добавлять только новые вакансии в вашу базу.


import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
from pymongo.errors import DuplicateKeyError

# Подготовим базу данных
client = MongoClient('localhost', 27017)
db = client['hh']  # hh - database
vacations = db.vacations  # vacations - collection

# функции для получения суммы заработка
def get_payment_min(s):
    res = ''
    if s.rfind('от')>=0:
        res = ''.join(filter(lambda i: i.isdigit(), s))
        return int(res)
    
    if s.rfind('–')>=0:
        res = s.split('–')[0]
        res = ''.join(filter(lambda i: i.isdigit(), res))
        return int(res)
    
def get_payment_max(s):
    res = ''
    if s.rfind('до')>=0:
        res = ''.join(filter(lambda i: i.isdigit(), s))
        return int(res)
    
    if s.rfind('–')>=0:
        res = s.split('–')[1]
        res = ''.join(filter(lambda i: i.isdigit(), res))
        # print(res)
        return int(res)

# функция для добавления данных в БД
def add_data_to_db(doc, only_new = True):
    exists = vacations.find_one({'link': doc['link']})
    if only_new == True:
        if not exists:
            try:
                vacations.insert_one(doc)
            except DuplicateKeyError:
                pass
    else:
        try:
            vacations.insert_one(doc)
        except DuplicateKeyError:
            pass

# Собираем и сохраняем данные
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
params = {'enable_snippets': False, 'text': 'Python', 'from': 'suggest_post', 'page': 1}
url = "https://rostov.hh.ru"
session = requests.Session()

while True:

    response = session.get(url+'/search/vacancy', headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    if not response.ok:
        break
    
    articles = soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})
    
    # проверка на наличие данных на станице
    if not articles:
        break

    for article in articles:
        article_info = {}

        info = article.find('h3')
        name = info.text
        link = info.find('a').get('href')

        b = info.parent

        payment = b.find_all("span")
        if str(payment).find('<!-- -->')>0:
            payment = payment[1].text.replace('\u202f','')
            payment_min = get_payment_min(payment)
            payment_max = get_payment_max(payment)
            payment_unit = payment[-1]
        else:
            payment = ""
            payment_min = None
            payment_max = None
            payment_unit = None

        article_info['name'] = name
        article_info['link'] = link
        article_info['payment_min'] = payment_min
        article_info['payment_max'] = payment_max
        article_info['unit'] = payment_unit

        add_data_to_db(article_info, only_new=True)

    print(f"Обработана страница №{params['page']}")
    params['page'] += 1

print ("Done!")