#importesinIVA = float(input("Importe sin IVA de un artículo: "))
#tipoIVA = float(input("Tipo de IVA a aplicar en %: "))
#importeconIVA = importesinIVA + (importesinIVA * tipoIVA/100)

#print("El precio final del artículo es de", importeconIVA, "€")

def importeconIVA(importesinIVA, tipoIVA):
    total = importesinIVA + (importesinIVA * tipoIVA/100)
    print(f"El precio final del artículo es de {total} €")

importesinIVA = float(input("Importe sin IVA de un artículo: "))
tipoIVA = float(input("Tipo de IVA a aplicar en %: "))

# Llama a la función para ejecutarla
importeconIVA(importesinIVA, tipoIVA)