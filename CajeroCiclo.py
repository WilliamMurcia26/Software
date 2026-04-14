saldo = 500000

while True:
    print("--- CAJERO ---")
    print("1. Ver saldo")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Tu saldo es: $", saldo)

    elif opcion == "2":
        cuenta = input("Ingresa el numero de cuenta destino: ")
        monto = int(input("Ingresa el monto a consignar: $"))
        if monto <= 0:
            print("Monto invalido.")
        elif monto > saldo:
            print("No tienes saldo suficiente. Operacion invalida.")
        else:
            saldo = saldo - monto
            print("Consignacion exitosa a la cuenta", cuenta)
            print("Nuevo saldo: $", saldo)

    elif opcion == "3":
        monto = int(input("Ingresa el monto a retirar: $"))
        if monto <= 0:
            print("Monto invalido.")
        elif monto > saldo:
            print("No tienes saldo suficiente. Operacion invalida.")
        else:
            saldo = saldo - monto
            print("Retiro exitoso.")
            print("Nuevo saldo: $", saldo)

    elif opcion == "4":
        print("Hasta luego.")
        break

    else:
        print("Opcion no valida, intenta de nuevo.")