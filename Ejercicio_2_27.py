nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
unidades = int(input("Ingrese el número de unidades: "))

coste_total = precio_unitario * unidades

print(f"Producto: {nombre_producto}")
print(f"Precio unitario: {precio_unitario:.2f}")
print(f"Número de unidades: {unidades:03d}")
print(f"Coste total: {coste_total:.2f}")