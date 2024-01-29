# Permite trabajar con solicitudes HTTP a las paginas web
import requests
# El módulo OS Path contiene algunas funciones útiles sobre nombres de rutas. 
from os import path
# Libreria que permite colocar opciones o argumentos cuando vallamos a ejecutar el programa
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Indica el dominio victima")
parser = parser.parse_args()

def main():
  # Si le pasamos una URL correcta 
  if parser.target:
    # Buscamos que el archivo subdominios.txt exista. Es el archivo que contiene todos los subdominios a probar
      if path.exists('subdominios.txt'):
          # Abrimos el archivo en modo lectura
          wordlist = open('subdominios.txt','r')
          # Leemos el archivo linea a linea
          wordlist = wordlist.read().split('\n')
          # Recorremos la lista
          for subdominio in wordlist:
            # armamos la url a probar
              url = "http://" + subdominio + "." + parser.target
              try:
                  # Respuesta 200
                  requests.get(url)
              except requests.ConnectionError:
                  # si el estado es un Error no hacemos nada
                  pass
              else: 
                  print("[+] Subdominio Descubierto: " + url)

          for subdominio in wordlist:
            url = "https://" + subdominio + "." + parser.target
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print("[+] Subdominio Descubierto: " + url)
  else:
      print("Porfavor coloca un subdominio valido")
      sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()