# Pseudocódigo:
# Inicio
#   Escribe "Ingresa el número de inicio: "
#   Lee inicio
#   Escribe "Ingresa el valor del incremento: "
#   Lee incremento
#   Escribe "Ingresa el total de la serie: "
#   Lee total_serie
#
#   Si incremento <= 0 O total_serie <= 0, entonces:
#       Escribir "Error: Tanto el incremento como el total deben ser mayores que cero."
#   Sino entonces
#       serie = [str(inicio)]
#       mientras inicio + incremento <= total_serie:
#           inicio += incremento
#           serie.append(str(inicio))
#       Escribe (f"SERIE => {'..'.join(serie)}")
# Fin

inicio = int(input("Ingresa el número de inicio: "))
incremento = int(input("Ingresa el valor del incremento: "))
total_serie = int(input("Ingresa el total de la serie: "))

if incremento <= 0 or total_serie <= 0:
    print("Error: Tanto el incremento como el total deben ser mayores que cero.")
else:
    serie = [str(inicio)]
    while inicio + incremento <= total_serie:
        inicio += incremento
        serie.append(str(inicio))
    print(f"SERIE => {'..'.join(serie)}")