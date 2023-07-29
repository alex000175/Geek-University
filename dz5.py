from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pprint import pprint
from pymongo import MongoClient
import time


# Подготовим базу данных
client = MongoClient('localhost', 27017)
db = client['letters']  # hh - database
letters = db.letters  # items - collection

# функция добавления данных в БД
def add_data_to_db(doc, only_new = True):
    exists = letters.find_one({'link': doc['link']})
    if only_new == True:
        if not exists:
            try:
                letters.insert_one(doc)
            except DuplicateKeyError:
                pass
    else:
        try:
            letters.insert_one(doc)
        except DuplicateKeyError:
            pass


s = Service('chromedriver')
chromeOptions = Options()
chromeOptions.add_argument('start-maximized')

drv = webdriver.Chrome(service=s, options=chromeOptions)
drv.implicitly_wait(0.2)
drv.get("https://account.mail.ru")

# авторизация
time.sleep(1)
elem = drv.find_element(By.NAME, 'username')
elem.send_keys("study.ai_172@mail.ru")
elem.send_keys(Keys.ENTER)

time.sleep(1)
elem = drv.find_element(By.NAME, 'password')
elem.send_keys("NextPassword172#")
elem.send_keys(Keys.ENTER)
time.sleep(1)


lettes_count_text = drv.find_element(By.XPATH, "//a[contains(@class,'nav__item')]").get_attribute('title')
res = (lettes_count_text.split(',')[1])
lettes_count = int(''.join(filter(lambda i: i.isdigit(), res)))
print(f'Всего писем в папке <Входящие>: {lettes_count}')


# сбор данных

# создаю и заполняю пустое множество для ссылок на письма
links = set() 
mails = drv.find_elements(By.CLASS_NAME, "js-letter-list-item")
link = mails[0].get_attribute('href')

while True:
    if len(links) >= lettes_count: # == lettes_count
        break
    
    mails = drv.find_elements(By.CLASS_NAME, "js-letter-list-item")
    for mail in mails:
        link = (mail.get_attribute('href'))
        links.add(link)

    action = ActionChains(drv)
    action.move_to_element(mails[-1])
    action.perform()

# заполняю БД данными
for link in links:
    info = {}
    drv.get(link)
    time.sleep(1) 
    # скорость соединения подводит, пришлось обернуть все вот в такой цикл
    num_retries = 0
    for i in range(1, num_retries+1):
        try:
            info['date'] = drv.find_element(By.XPATH, "//div[@class='letter__date']").text.split(',')[0]
            info['from_email'] = info['from_email'] = drv.find_element(By.XPATH, "//span[contains(@class, 'letter-contact')]").get_attribute('title')
            info['author'] = drv.find_element(By.XPATH, "//span[contains(@class,'letter-contact')]").text
            info['subject'] = drv.find_element(By.XPATH, "//h2[@class='thread-subject']").text
            info['body'] = drv.find_element(By.XPATH, "//div[@class='letter__body']").text
            info['link'] = link
            add_data_to_db(info)
            break
        except:
            time.sleep(1)
            num_retries += 1
drv.close()

# Проверяем, что данные в БД
for item in letters.find({}):
    pprint(item)
