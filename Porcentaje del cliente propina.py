total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (%): "))

monto_propina = total_cuenta * (porcentaje_propina / 100)

total_final = total_cuenta + monto_propina

print("Total de la cuenta: ", total_cuenta)
print("Porcentaje de propina: ", porcentaje_propina, "%")
print("Monto de la propina: ", monto_propina)
print("Total a pagar: ", total_final)