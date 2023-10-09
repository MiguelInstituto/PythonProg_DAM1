capital = float(input("Introduzca el capital deseado en euros: "))
interés = capital * (1 + 0.04)
interés1año = interés*1
interés2años = interés*2
interés3años = interés*3
print("La cantidad de ahorros en un año es de {:.2f} €, en dos años de {:.2f} € y tras tres años de {:.2f} €".format(interés1año, interés2años, interés3años))