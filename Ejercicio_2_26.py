productos = input("Ingrese los productos de la cesta de compra separados por comas: ")
productos_lista = productos.split(',')

for producto in productos_lista:
    print(producto.strip())  # Elimina espacios en blanco alrededor del producto