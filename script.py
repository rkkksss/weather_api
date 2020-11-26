import requests
from requests.exceptions import HTTPError as error

cities = ['Лондон', 'Шереметьево', 'Череповец']
payload = {'n': '', 'T': '', 'q': '', 'u': '', 'm': '', 'lang': 'ru'}


for city in cities:
    url = 'http://wttr.in/{}'.format(city)
    response = requests.get(url, params=payload)
    try:
        response.raise_for_status()
        print(response.text)
    except error:
        print(f'Прогноз недоступен, код ошибки: {error}')
