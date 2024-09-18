# Definir las constantes
BONIFICACION = 2400.0
INACEPTABLE = 0.0
ACEPTABLE = 0.4
MERITORIO = 0.6

# Leer la puntuación del usuario
puntuacion = float(input("Introduce tu puntuación: "))

# Determinar el nivel de rendimiento
if puntuacion == INACEPTABLE:
    rendimiento = "Inaceptable"

elif puntuacion == ACEPTABLE:
    rendimiento = "Aceptable"

elif puntuacion >= MERITORIO:
    rendimiento = "Meritorio"

else:
    rendimiento = "Puntuación no válida"

# Calcular la cantidad de dinero
dinero = BONIFICACION * puntuacion

# Mostrar los resultados
if rendimiento == "Puntuación no válida":
    print("Esta puntuación no es válida.")

else:

    print(f"Tu nivel de rendimiento es: {rendimiento}")

    print(f"Te corresponde cobrar: ${dinero:.2f}")

