#gcelsius = float(input("Temperatura en grados celsius: "))
#gfahrenheit = (gcelsius * 9 / 5) + 32

#print("La temperatura es de", gfahrenheit, "°F")

def gfahrenheit(gcelsius):
    return (gcelsius * 9 / 5) + 32

gcelsius = float(input("Temperatura en grados celsius: "))
print(f"La temperatura es de {gfahrenheit(gcelsius)} °F")