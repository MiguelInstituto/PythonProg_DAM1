peso = float(input("¿Cuál es tu peso en kilogramos? "))
estatura = float(input("¿Cuál es tu altura en metros? "))
IMC = peso/((estatura)**2)
print("Tu índice de masa corporal, siendo redondeado con dos decimales es de, {:.2f}".format(IMC))