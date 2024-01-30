# Validamos si el sitio web tiene el WAF CloudFlare
import requests
import sys

def main():
  webSite = input("Ingresa el sitio web (e.g https://ejemplo.com) \n=>")
  palabra = "cloudflare"
  url = requests.get(webSite)
  cabeceras = dict(url.headers)
  verificacion = False
  for cabecera in cabeceras:
    if palabra in cabeceras[cabecera].lower():
      verificacion = True
      break

  if verificacion == True:
    print("El sitio web tiene CloudFlare")
  else:
    print("El sitio no tiene Cloudflare")


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()