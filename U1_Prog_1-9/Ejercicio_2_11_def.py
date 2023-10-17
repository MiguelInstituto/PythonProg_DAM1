#n = int(input("Introduce un número entero positivo "))
#if n < 1:
    #n = int(input("Número erróneo"))
#else:
    #suma = (n*(n+1))/2
    #print(suma)

def calcular_suma_de_enteros_positivos(n):
    if n < 1:
        return print("Número erróneo. Debe ser un entero positivo.")
    else:
        suma = (n * (n + 1)) / 2
        return print("La suma de los números enteros positivos desde 1 hasta", n, "es:", suma)

n = int(input("Introduce un número entero positivo: "))

# Llama a la función para ejecutarla
calcular_suma_de_enteros_positivos(n)