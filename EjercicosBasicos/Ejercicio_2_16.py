panbarradia = 3.49
descuento = 60
panbarranodia = panbarradia - (panbarradia * descuento/100)
panbarranodiacantidad = int(input("Introduce el número de barras vendidas que no son del día "))
panbarranodiaventas = panbarranodia * panbarranodiacantidad

print("El precio habitual de una barra de pan es de {:.2f} €, el descuento que se le hace por no ser fresca es del {} % y el coste final total de todas las barras no frescas es de {:.2f} €".format(panbarradia, descuento, panbarranodiaventas))