import hashlib

# Solicitar el hash objetivo y el archivo del diccionario
hash_file = input("Ingrese el hash objetivo: ").strip()
dic_file = input("Ingrese la dirección del archivo del diccionario: ").strip()

try:
    # Abrir el diccionario de contraseñas y procesar línea por línea
    with open(dic_file, 'r') as file:
        encontrado = False
        for i, password in enumerate(file):
            password = password.strip()
            hash_calculado = hashlib.sha256(password.encode()).hexdigest()
            
            # Comparar el hash calculado con el hash objetivo
            if hash_calculado == hash_file:
                print(f"La contraseña original es: {password}")
                encontrado = True
                break

            # Mostrar progreso cada 1000 intentos
            if i % 1000 == 0:
                print(f"Intentos procesados: {i}")

        # Si no se encontró ninguna coincidencia
        if not encontrado:
            print("La contraseña no se encuentra en el diccionario.")
except FileNotFoundError:
    print("Error: El archivo del diccionario no existe.")
except Exception as e:
    print(f"Error inesperado: {e}")
