lado = float(input("Ingresa el valor del lado del cuadrado: "))

if lado > 0:
    area_cuadrado = lado * lado
    print("El área del cuadrado es en cm²:", area_cuadrado)
else:
    print("Error: El lado debe ser un número positivo")

if area_cuadrado <= 100:
    print("El area es menor a 100 cm²")
    print("Tienes un cuadrado pequeño bro")
else:
    print("El area es mayor a 100 cm²")
    print("Tienes un cuadrado re grande bro")