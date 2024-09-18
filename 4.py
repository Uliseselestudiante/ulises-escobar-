# Preguntar al como se llama y si es hombre o mujer
nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo (M para mujer, H para hombre)? ")

# Determinar el grupo
if (sexo == "M" and nombre.lower() < "m") or (sexo == "H" and nombre.lower() > "n"):
    grupo = "A"
else:
    grupo = "B"

# Mostrar el grupo al que pertenece el usuario
print("Tu grupo es:", grupo)
