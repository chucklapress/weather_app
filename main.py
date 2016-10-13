import requests
from pprint import pprint
zc = input(' zipCode')
url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zc + ',us &>>>>>'

response = requests.get(url)
pprint(response.json())
