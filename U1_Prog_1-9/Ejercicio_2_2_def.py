def impTotal(horas, coste):
    return horas * coste

horas = int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))

print("El importe total es de: " + str(impTotal(horas, coste)))