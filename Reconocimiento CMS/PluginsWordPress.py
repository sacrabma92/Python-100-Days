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
      lista_plugin.append(plugin)

  for i in lista_plugin:
    if i in lista_final:
      pass
    else:
      lista_final.append()

  for i in lista_final:
    print("[+] Se encontro el plugin {i}".format(i))

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()