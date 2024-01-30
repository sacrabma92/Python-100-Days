import requests
import sys
from bs4 import BeautifulSoup
import time

def main():
  url = input("Ingresa el sitio web\n")
  agent = {'User-Agent':'Firefox'}
  peticion = requests.get(url=url,headers=agent)
  soup = BeautifulSoup(peticion.text, 'html.parser')

  lista_1 = []
  lista_temas = []

  for enlace in soup.find_all('link'):
    if '/wp-content/themes' in enlace.get('href'):
      href = enlace.get('href')
      href = href.split('/')
      if 'themes' in href:
        posicion = href.index('themes')
        tema = href[posicion + 1]
        lista_1.append(tema)

  for tema in lista_1:
    if tema in lista_temas:
      pass
    else:
      lista_temas.append(tema)

  for tema in lista_temas:
    print(f"[+] Se encontro el tema: {tema}")
    time.sleep(1)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()
  