import requests
# libreria que detecta que los parametros que se pasan por consola.
import argparse

# Encabezado que se imprime cuando se proporciona el argumento -h
parser = argparse.ArgumentParser(description="Detector de comandos")
# argumento -t para especificar el target
parser.add_argument('-t','--target',help="Valor")
parser = parser.parse_args()

# Si le pasamos algun parametro
if parser.target:
  try:
    # Obtenemos por metodo GET la url que le estamos pasando
    url=requests.get(url=parser.target)
    # Almacenamos la respuesta en la variable header
    header=dict(url.headers)
    # Recorremos toda las lineas de codigo y las imprimimos, esto es para que se vea mejor en la consola.
    for x in header:
      print(x + " : " + header[x])
  except:
    print("Error de conexion.")
# Si no ingresamos parametros extras
else:
  print("No has especificado nada")