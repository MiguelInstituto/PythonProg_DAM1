telefono = input("Ingrese un número de teléfono en formato +34-xxxxxxxxx-xx: ")
numero = telefono[4:13]  # Extraer el número sin prefijo y extensión

print("Número de teléfono sin prefijo y extensión:", numero)