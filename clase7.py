"""Clase 7 Soltero, Viudo"""
flag = False
descuento = "TATATATATATATA"
edad = int(input("Ingrese su edad: "))
estado = input("Cual es su estado civil (Soltero, Casado, Divorciado, Viudo): ")
socio = input("Es usted socio (S/N): ")
if edad > 70:
    if estado.upper() == "SOLTERO" or estado.upper() == "VIUDO":
        descuento = "15%"
    elif estado.upper() == "CASADO" or estado.upper() == "DIVORCIADO":
        descuento = "10%"
elif edad <= 69 and edad >= 25:
    if estado.upper() == "SOLTERO" or estado.upper() == "VIUDO":
        descuento = "5%"
    elif estado.upper() == "CASADO" or estado.upper() == "DIVORCIADO":
        descuento = "3%"
else:
    flag = True
if flag is True:
    if socio.upper() == "S":
        print("Cuenta con un descuento del 8%")
    else:
        print("No cuenta con descuento")
else:
    if socio.upper() == "S":
        print(f"Cuenta con un descuento del {descuento} mas un descuento del 8%")
    else:
        print(f"Cuenta con un descuento del {descuento}")
