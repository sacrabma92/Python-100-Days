import requests
import sys
from os import path

def main():
  if path.exists('wp-plugins.txt'):
    file = open("wp-plugins.txt",'r',encoding="utf-8")
    file = file.read().split("\n")
    lista = []

    url = "https://anormalix.com"# input("Ingresa una URL => ")

    for plugin in file:
      url_final = url +"/"+plugin
      peticion = requests.get(url=url_final)
      
      if peticion.status_code == 200:
        print("[+] Succed: "+url_final)
        url_final = url_final.split('/')
        posicion = url_final.index('plugins')
        plugin_encontrado = url_final[posicion+1]
        lista.append(url_final)
      
    print("="*50)
    for i in lista:
      print("[+] Se encontro el plugin: {}".format(i))

  else:
    print("[!] El archivo wp-plugins.txt NO existe")

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()