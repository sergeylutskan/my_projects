###################################
# Простая программа, с помощью API достающая из ЕГРЮЛ адреса филиалов Предприятия
#
# Receives information from the state information system of the Federal tax service using API
#
###################################

import requests
import time

api_url = 'https://api-fns.ru/api/egr'
api_key = 'your_api_key_for_service'
OGRN = '1111111111' #Regnumber of organization

params = {
    'req' : OGRN,
    'key' : api_key,
}

res = requests.get(api_url,params=params)
data = res.json()
for i in data['items'][0]['ЮЛ']['Филиалы']:
    print(i['Адрес'])


