# Написать приложение, которое собирает основные новости с сайта на выбор 
# news.mail.ru, lenta.ru, yandex-новости. 
# Для парсинга использовать XPath
# Сложить собранные новости в БД

import requests
import locale

from lxml import html
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pprint import pprint
from datetime import date

locale.setlocale(locale.LC_TIME, 'ru')

# Подготовим базу данных
client = MongoClient('localhost', 27017)
db = client['news']  # hh - database
my_news = db.my_news  # items - collection

# функция добавления данных в БД
def add_data_to_db(doc, only_new = True):
    exists = my_news.find_one({'link': doc['link']})
    if only_new == True:
        if not exists:
            try:
                my_news.insert_one(doc)
            except DuplicateKeyError:
                pass
    else:
        try:
            my_news.insert_one(doc)
        except DuplicateKeyError:
            pass


# Получаем данные со страницы
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url = "https://lenta.ru"
session = requests.Session()

response = session.get(url+'/parts/news', headers=headers)

# https://lenta.ru/parts/news/
print(f'URL is {response.url}')
print(f'Status code is {response.status_code}')

dom = html.fromstring(response.text)

items = dom.xpath("//li[@class='parts-page__item']")
# all_news = []
for item in items:
    news = {}
    resource = url
    name = item.xpath(".//h3[@class='card-full-news__title']/text()")
    link = item.xpath(".//h3[@class='card-full-news__title']/../@href")
    news_time = item.xpath(".//time[contains(@class,'card-full-news__date')]/text()")
    

    news['resource'] = resource
    news['name'] = ''.join(name)
    
    if 'https' in str(link):
        news['link'] = ''.join(link)
    else:
        news['link'] = url + ''.join(link)
    
    if len(''.join(news_time))<10:
        news['news_time'] = ''.join(news_time) + ', ' + date.today().strftime("%d %B %Y")
    else:
        news['news_time'] = ''.join(news_time)


    add_data_to_db(news, only_new=True)


# Проверяем, что данные в БД
for item in my_news.find({'resource': url}):
    pprint(item)