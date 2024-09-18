# Precio de cada zapato
precio_zapato = 80

# Preguntamos al usuario cuántos zapatos va a comprar
cantidad_zapatos = int(input("¿Cuántos zapatos quieres comprar? "))

# Calculamos el total sin descuento
total = cantidad_zapatos * precio_zapato

# Aplicamos el descuento según la cantidad de zapatos comprados
if cantidad_zapatos > 30:
    descuento = 0.40
elif cantidad_zapatos > 20:
    descuento = 0.20
elif cantidad_zapatos > 10:
    descuento = 0.10
else:
    descuento = 0.0

# Calculamos el total con descuento
total_con_descuento = total * (1 - descuento)

# Mostrar el total a pagar
print("El total a pagar es: $", total_con_descuento)

