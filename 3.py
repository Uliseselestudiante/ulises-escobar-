# Almacenamos la contraseña en una variable
contraseña_guardada = "Patriota"

# Preguntamos al usuario la contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# Vemos si la contraseña es la  misma (sin tener en cuenta mayúsculas y minúsculas)
if contraseña_guardada.lower() == contraseña_usuario.lower():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

