"""clase 11"""
saldo = 100000
movimientos = []
while True:
    print("""
              Sistema bancario
              1) Girar
              2) Depositar
              3) Estado de cuenta
              4) Salir
              """)
    try:
        op = int(input("Ingrese su seleccion: "))
        match op:
            case 1:
                print("Girar dinero")
                if saldo >= 5000:
                    while True:
                        try:
                            sacar = int(input("Cuanto dinero desea sacar: "))
                            if sacar > saldo:
                                print("Excede su saldo actual")
                            elif sacar < 5000:
                                print("No puede sacar menos de $5000")
                            else:
                                saldo -= sacar
                                print(f"Nuevo saldo: ${saldo}")
                                movimientos.append(f"Retiro: ${sacar}")
                                break
                        except ValueError:
                            print("Monto debe ser un numero")
                else:
                    print("No tiene saldo suficiente para retirar")
            case 2:
                print("Deposito")
                while True:
                    try:
                        depositar = int(
                            input("Ingrese la cantidad de dinero que quiere depositar: "))
                        if depositar > 1000 <= 300000:
                            saldo += depositar
                            print(f"Nuevo saldo: ${saldo}")
                            movimientos.append(f"Deposito: ${depositar}")
                            break
                        else:
                            print(
                                "El deposito debe ser mayor a $1000 y menor a $300000")
                    except ValueError:
                        print("Monto debe ser un numero")
            case 3:
                print("Estado de cuenta")
                print(f"Saldo actual: ${saldo}")
                if len(movimientos) > 0:
                    print("Movimientos: ")
                    for movs in movimientos:
                        print(movs)
                else:
                    print("No a tenido movimientos aun")
            case 4:
                print("Gracias por usar")
                break
            case _:
                print("No existe alguna opcion asi")
    except ValueError:
        print("Debe ingresar un numero")
