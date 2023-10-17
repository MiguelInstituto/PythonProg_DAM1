#gcelsius = float(input("Temperatura en grados celsius: "))
#gfahrenheit = (gcelsius * 9 / 5) + 32

#print("La temperatura es de", gfahrenheit, "°F")

def gfahrenheit():
    gcelsius = float(input("Temperatura en grados celsius: "))
    return (gcelsius * 9 / 5) + 32


print(f"La temperatura es de {gfahrenheit()} °F")