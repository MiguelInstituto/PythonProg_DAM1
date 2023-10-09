correo = input("Ingrese su correo electrónico: ")
nombre = correo.split('@')[0]
nuevo_correo = nombre + '@ceu.es'

print("Nuevo correo electrónico:", nuevo_correo)