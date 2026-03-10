#Clasificaon ventas(Baja, Media,Alta)

ventas = [12000, 8000, 15000, 4000, 22000, 7000, 18000]

ventas_altas = 0

for i in range(len(ventas)):
    venta = ventas[i]

    if venta < 7000:
        print(i+1, "-", venta, "- Venta baja")
        
    elif 7000 <= venta <= 15000:
        print(i+1, "-", venta, "- Venta media")
        
    else:
        print(i+1, "-", venta, "- Venta alta")
        ventas_altas += 1

print("Total de ventas altas:", ventas_altas)