preciofinal = float(input("Precio final de un artículo: "))
tipoIVA = 10
importesinIVA = preciofinal - (preciofinal * tipoIVA/100)

print("El importe sin IVA es de {:.2f} €".format(importesinIVA))