n = int(input("Introduce un número entero positivo "))
if n < 1:
    n = int(input("Número erróneo"))
else:
    suma = (n*(n+1))/2
    print(suma)