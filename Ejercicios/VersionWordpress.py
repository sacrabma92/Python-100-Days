import requests
from bs4 import BeautifulSoup

url = "https://www.tectroya.cl/"
headers = {'User-Agent':'Firefox'}
peticion = requests.get(url=url,headers=headers)

soup = BeautifulSoup(peticion.text, 'html5lib')
for i in soup.find_all('meta'):
  if i.get('name') == 'generator':
    version = i.get('content')
    print(version)