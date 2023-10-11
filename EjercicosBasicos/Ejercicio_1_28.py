# Pseudocódigo:
# Inicio
#   Escribe "Ingrese el primer número entero: "
#   Lee num1
#   Escribe "Ingrese el segundo número entero: "
#   Lee num2
#   Si (num1 == num2), entonces 
#       Escribe "Error: Los números no pueden ser iguales"
#   Sino entonces
#       Lee menor = min(num1, num2)
#       Lee mayor = max(num1, num2)
#       Lee cantidad_numeros = mayor - menor - 1
#       Escribe "El número menor es el {menor} y entre ellos existen {cantidad_numeros} números enteros.""
# Fin

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 == num2:
    print("Error: Los números no pueden ser iguales")
else:
    menor = min(num1, num2)
    mayor = max(num1, num2)
    cantidad_numeros = mayor - menor - 1
    print(f"El número menor es el {menor} y entre ellos existen {cantidad_numeros} números enteros.")