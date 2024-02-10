import requests
from bs4 import BeautifulSoup

url = "https://www.textroya.cl/"
headers = {'User-Agent':'Firefox'}
peticion = requests.get(url=url, headers=headers)
soup = BeautifulSoup(peticion.text, 'html5lib')


for i in soup.find_all('link'):
  if '/wp-content/themes' in i.get('href'):
      theme = i.get('href')
      theme = theme.split('/')
      if 'themes' in theme:
         posicion = theme.index('themes')
         temple = theme[posicion + 1]
         print("El tema en uso es: " + temple)
         break