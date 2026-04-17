"""CALCULADORA DE LOS COJINES"""
while True:
    print("Calculadora")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    op = int(input("Escoga del 1-5: "))
    match op:
        case 1:
            a = float(input("Introduzca el primer numero a operar: "))
            b = float(input("Introduzca el segundo numero a operar: "))
            c = a + b
            print("El resultado de tu operación es: ", c)
        case 2:
            a = float(input("Introduzca el primer numero a operar: "))
            b = float(input("Introduzca el segundo numero a operar: "))
            c = a - b
            print("El resultado de tu operación es: ", c)
        case 3:
            a = float(input("Introduzca el primer numero a operar: "))
            b = float(input("Introduzca el segundo numero a operar: "))
            c = a * b
            print("El resultado de tu operación es: ", c)
        case 4:
            a = float(input("Introduzca el primer numero a operar: "))
            b = float(input("Introduzca el segundo numero a operar: "))
            if b != 0:
                c = a / b
                print("El resultado de tu operación es: ", c)
            else:
                print("No se puede dividir por 0")
        case 5:
            print("Saliendo del sistema")
            break
        case _:
            print("Opcion invalida")
