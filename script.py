import requests

cities = ['London', 'Sheremetyevo', 'Cherepovets']
settings = {'m': '', 'n': '', 'T': '', 'q': '', 'lang': 'ru'}
url_template = 'https://wttr.in/{}'
for city in cities:
  response = requests.get(url_template.format(city), settings)
  print(response.text)
