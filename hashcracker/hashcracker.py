import hashlib

hash_file = "b460b1982188f11d175f60ed670027e1afdd16558919fe47023ecd38329e0b7f"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

encontrado = False
with open(dic_file, 'r') as file:
    diccionario = [line.strip() for line in file]

    
    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        
        if hash_calculado == hash_file:
            print("La contraseña original es: " + password)
            encontrado = True
            break

if encontrado == False:
    print("La contraseña no se encuentra en el diccionario")