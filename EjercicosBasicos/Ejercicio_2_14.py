pesopayaso = int(112)
pesomuñeca = int(75) 
cantidadpayasos = int(input("Introduzca la cantidad de payasos que serán enviados en el paquete "))
cantidadmuñecas = int(input("Introduzca la cantidad de muñecas que serán enviadas en el paquete "))
pesototal = (cantidadpayasos * pesopayaso) + (cantidadmuñecas * pesomuñeca)
print(f"El peso total del paquete que será enviado es de {pesototal} gramos")