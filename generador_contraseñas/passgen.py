import string
import random
import os

long = int(input("Ingrese el tamaño de la contraseña: "))
caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(long))

print("La contraseña generada es: " + contraseña)

concepto = input("Introduce de dónde va a ser la contraseña (Instagram, Correo, ...): ")

ruta = os.path.join(os.path.dirname(__file__), "lista_contraseñas.txt")
with open(ruta, "a", encoding="utf-8") as f:
    f.write(f"{concepto} : {contraseña}\n")