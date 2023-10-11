# Pseudocódigo:
# Inicio
#   Escribe "Ingresa tu nombre: "
#   Lee nombre
#   Si nombre  == "", entonces
#       "Desconocido" como valor
#   Mientras sea cierto
#       Intenta leer edad
#           Si edad  0 <= edad <= 125, entonces:
#               Rompe el bucle
#           Si no entonces: 
#               Escribe "Edad no válida. Debe estar entre 0 y 125 años."
#       Excepto edad == ValueError, entonces:
#           Escribe "Ingresa un número válido para la edad."
#   años_restantes = 125 - edad
#   Escribe "Te llamas {nombre} y tienes {edad} años, te quedan aún {años_restantes} años por cumplir."
# Fin

nombre = input("Ingresa tu nombre: ")
if nombre == "":
    nombre = "Desconocido"

while True:
    try:
        edad = int(input("Ingresa tu edad (entre 0 y 125 años): "))
        if 0 <= edad <= 125:
            break
        else:
            print("Edad no válida. Debe estar entre 0 y 125 años.")
    except ValueError:
        print("Ingresa un número válido para la edad.")

años_restantes = 125 - edad
print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años_restantes} años por cumplir.")