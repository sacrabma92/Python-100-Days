import requests
import sys
from bs4 import BeautifulSoup

def main():
  url = "https://web.com"
  agent = {'User-Agent':'Firefox'}
  peticion = requests.get(url=url,headers=agent)
  soup = BeautifulSoup(peticion.text,'html.parser')

  for enlace in soup.find_all('link'):
    if 'wp-content/plugins' in enlace.get('href'):
      href = enlace.get('href')
      href = href.split('/')
      posicion = href.index('plugins')
      plugin = href[posicion+1]
      print(plugin)


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()