# Изучить список открытых API (https://www.programmableweb.com/category/all/apis). 
# Найти среди них любое, требующее авторизацию (любого типа). 
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл


# $ pip install vk

import vk
import json

# Тут токен доступа:
token = 'токен'

session = vk.Session(access_token=token)
api = vk.API(session)

# Получим айдишники моих друзей вконтакте: (https://vk.com/cuss17)
f = api.friends.get(user_id=352043580, v=5.131)
print(f)

# Запишем полученные айдишники в файл
with open('my_friends_id.json', 'w') as file:
    json.dump(f, file)
