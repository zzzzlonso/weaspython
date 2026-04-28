"""Ejercicio de numeros"""
# while True:
#     num1 = int(input("Ingrese un numero cualquiera: "))
#     if num1 >= 0:
#         print("Puede continuar")
#         break
#     else:
#         print("No podra avanzar hasta que ingrese un numero positivo: ")
# if num1 % 2 == 0:
#     print("Su numero es par")
# else:
#     print("Su numero es impar")
################################################
# numero = None
# while True:
#     print("1) Ingresar Numero \n2) Mostrar Numero \n3) Mostrar doble de su numero \n4) Salir")
#     op = int(input("Ingrese su eleccion(1-4): "))
#     match op:
#         case 1:
#             numero = int(input("Ingrese su numero"))
#         case 2:
#             if numero is None:
#                 print("Aun no a ingresado ningun numero")
#             else:
#                 print(f"Su numero es {numero}")
#         case 3:
#             if numero is None:
#                 print("Aun no a ingresado ningun numero")
#             else:
#                 print(f"El doble de su numero es {numero * 2}")
#         case 4:
#             print("Xao bb que te vaya bien")
#             break
######################################################################
useradmin = "admin"
password = "1234"
i = 0
flag = False
while i <= 2:
    user = input("Ingrese su nombre de usuario: ")
    passworduser = input ("Ingrese su contraseña: ")
    if user == useradmin and passworduser == password:
        i = 3
        flag = True
    else:
        i = i + 1
        print(f"Le quedan {3-i} intentos")
if flag is True:
    print("Bienvenido brodel")
else:
    print("Cuenta bloqueda")
