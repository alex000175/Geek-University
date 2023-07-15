import requests
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint

def get_payment_min(s):
    res = ''
    if s.rfind('от')>=0:
        res = ''.join(filter(lambda i: i.isdigit(), s))
        return res
    
    if s.rfind('–')>=0:
        res = s.split('–')[0]
        res = ''.join(filter(lambda i: i.isdigit(), res))
        return res
    
def get_payment_max(s):
    res = ''
    if s.rfind('до')>=0:
        res = ''.join(filter(lambda i: i.isdigit(), s))
        return res
    
    if s.rfind('–')>=0:
        res = s.split('–')[1]
        res = ''.join(filter(lambda i: i.isdigit(), res))
        # print(res)
        return res
    

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
params = {'enable_snippets': False, 'text': 'Python', 'from': 'suggest_post', 'page': 1}
url = "https://rostov.hh.ru"
session = requests.Session()

articles_list = []


response = session.get(url+'/search/vacancy', headers=headers, params=params)

while response.status_code == 200:
    # if params['page'] == 2:
    #     break

    response = session.get(url+'/search/vacancy', headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})
    
    for article in articles:
        article_info = {}

        info = article.find('h3')
        name = info.text
        link = info.find('a').get('href')

        b = info.parent
        # payment = b.find_all("span")[1].text.replace('\u202f','')

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
        articles_list.append(article_info)

    print(f"Обработана страница №{params['page']}")
    params['page'] += 1

df = pd.DataFrame({
        "Название вакансии": [],
        "Зарплата от": [],
        "Зарплата до": [],
        "Валюта": [],
        "Ссылка": []
    }) 
n = 0
for i in articles_list:
    n += 1
    df.loc[n] = [i['name'], i['payment_min'], i['payment_max'], i['unit'], i['link']]  # adding a row



file_name1 = 'vacansions.xlsx'
with pd.ExcelWriter(file_name1) as writer:
    df.to_excel(writer, sheet_name="Список", index=True) 

df.to_csv('vacansions.csv')

