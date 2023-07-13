# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, 
# сохранить JSON-вывод в файле *.json

import requests
import json

url = 'https://api.github.com'
user = 'alex000175'
req = requests.get(f'{url}/users/{user}/repos')

for i in req.json():
    print(i['name'])


with open('data.json', 'w') as f:
    json.dump(req.json(), f)


