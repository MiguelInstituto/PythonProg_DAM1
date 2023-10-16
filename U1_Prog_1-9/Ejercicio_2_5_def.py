#importesinIVA = float(input("Importe sin IVA de un artículo: "))
#tipoIVA = float(input("Tipo de IVA a aplicar en %: "))
#importeconIVA = importesinIVA + (importesinIVA * tipoIVA/100)

#print("El precio final del artículo es de", importeconIVA, "€")

def importeconIVA(importesinIVA, tipoIVA):
    return importesinIVA + (importesinIVA * tipoIVA/100)

importesinIVA = float(input("Importe sin IVA de un artículo: "))
tipoIVA = float(input("Tipo de IVA a aplicar en %: "))
print(f"El precio final del artículo es de {importeconIVA(importesinIVA, tipoIVA)} €")