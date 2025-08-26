import socket

def validacion(result, puerto):
    if result ==0:
        print("Este puerto está abierto: " + str(puerto))

    else:
        print("Puerto cerrado: " + str(puerto))


ip = input("Ingrese la dirección IP a escanear: ")

while True:
    opcion = int(input("Ingresa 1 para preguntar por un puerto específico o 2 para ir recorriendo todos los puertos uno por uno: "))

    if opcion == 1:
        p = int(input("Ingresa el puerto por el que quieras preguntar: "))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((ip, p))
        validacion(result,p)
        sock.close()

    elif opcion ==2:
        for puerto in range(1,65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, puerto))

            validacion(result,puerto)
            sock.close()

    else:
        print("Ingrese 1 o 2, otras entradas no serán aceptadas.")




    
        