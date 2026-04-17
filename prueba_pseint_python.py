"""PRUEBA"""
edad = int(input("Ingrese su edad: "))
ingreso = input("Se habia registrado con anterioridad(SI/NO): ")
if edad >= 18:
    if ingreso.upper() == "SI":
        print("Ingreso aceptado")
    else:
        print("Ingreso denegado")
else:
    print("Debe ser mayor de edad para ingresar")
