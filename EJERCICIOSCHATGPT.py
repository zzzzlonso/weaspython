"""Ejercicios de chatGPT"""

# n1 = int(input("Ingrese el primer número: "))
# n2 = int(input("Ingrese el segundo número: "))
# if n1 == n2:
#     print("Los números son iguales.")
# elif n1 > n2:
#     print("El numero mayor es: ", n1)
# else:
#     print("El numero mayor es: ", n2)

"""EJERCICIO 2 Contar numeros positivos"""

# contadorpositivo = 0
# contadornegativo = 0   
# contador0 = 0
# op = int(input("Ingrese la cantidad de números a ingresar: "))
# for i in range(op):
#     num = int(input("Ingrese un número: "))
#     if num > 0:
#         print("El número es positivo.")
#         contadorpositivo = contadorpositivo + 1
#     elif num < 0:
#         print("El número es negativo.")
#         contadornegativo = contadornegativo + 1
#     else:
#         print("El número es cero.")
#         contador0 = contador0 + 1    

# print("Cantidad de números positivos:", contadorpositivo)
# print("Cantidad de números negativos:", contadornegativo)
# print("Cantidad de números cero:", contador0)

"""Ejercicio, JUEGO MAYOR MENOR"""
# import random
# n1 = random.randint(1, 1000)
# print("Bienvenido al juego de mayor o menor")
# print("Estoy pensando en un número entre 1 y 1000. ¿Puedes adivinar cuál es?")
# while True:
#     adivina = int(input("Ingresa tu adivinanza: "))
#     if adivina < n1:
#         print("El número es mayor. Intenta de nuevo.")
#     elif adivina > n1:
#         print("El número es menor. Intenta de nuevo.")
#     else:
#         print("¡Felicidades! Has adivinado el número.")
#         break
"""Ejercicio, promedio de notas y mayor o menor nota"""
numero = []
caca = int(input("Ingrese la cantidad de notas a ingresar: "))
for i in range(caca):
    nota = float(input("Ingrese la nota: "))
    numero.append(nota)

promedio = sum(numero) / len(numero)
print("El promedio de las notas es:", promedio)

mayor = max(numero)
menor = min(numero)
print("La mayor nota es:", mayor)
print("La menor nota es:", menor)