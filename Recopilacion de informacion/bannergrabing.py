import socket
import sys

def banner(ip, puerto):
  # Creamos la varible para pasarle parametros
  s = socket.socket()
  # Entablamos la conexion a la IP en el Puerto
  s.connect((ip, puerto))
  # Recibira un maximo de 1024
  print(str(s.recv(1024)))

def main():
  # Ingresamos la IP
  ip = input("Ingresa la Ip objetivo: ")#"192.168.2.49"
  # Ingresamos el Port
  port = int(input("Ingresa el puerto: "))#22
  # Llamamos el metodo banner() y le pasamos la Ip y Port
  banner(ip,port)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt():
    sys.exit()