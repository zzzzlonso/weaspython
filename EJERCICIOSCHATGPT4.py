# """Ejercicios python"""
# from random import randint
# num = randint(1, 50)
# while True:
#     num1 = int(input("Ingrese un numero entre 1 y 50: "))
#     if num == num1:
#         print("Ganaste 🥹🔥🙌")
#         break
#     elif num1 < num:
#         print("El numero es mayor vuelva a ingresar")
#     elif num1 > num:
#         print("El numero es menor vuelva a ingresar")
        
# """Ejercicio 2"""
# from random import choice
# contador = 0
# op = "S"
# Numeros = [2, 48, 39, 87, 93, 56 ]
# num = choice(Numeros)
# while True:
#     num1 = int(input("Ingrese un numero: "))
#     contador += 1
#     if num == num1:
#         print(f"Ganaste 🥹🔥🙌, Lo lograste en {contador} intentos")
#         break
#     if num1 < num:
#         print("El numero es mayor vuelva a ingresar")
#     elif num1 > num:
#         print("El numero es menor vuelva a ingresar")
# """Ejercicio 3"""
# from random import choice
# nombres = ["CHATGPT", "GEMINI AI" ,"Ignacio" ,"WAZA" , "Alonso" ]
# while True:
#     if len(nombres) == 1:
#         break
#     eliminado = choice(nombres)
#     nombres.remove(eliminado)
#     print(f"El nombre eliminado en esta ocasion fue {eliminado}")
#     input("Ingrese cualquier tecla para continuar: ")
# print(f"El nombre ganador fue: {nombres}")
"""Ejercicio 4 pormi DIGITO DEL RUT"""
rut = (input("Ingrese su rut sin digito verificador: "))
suma = 0
multi = 2
for d in rut[::-1]:
    suma += int(d) * multi
    multi += 1
    if multi > 7:
        multi = 2
resto = suma % 11
digito = 11 - resto
if digito == 11: 
    print("Su digito verificador es: 0")
elif digito == 10:
    print("Su digito verificador es: K")
else:
    print(f"Su digito verificador es: {digito}")
