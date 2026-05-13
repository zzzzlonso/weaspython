"""Clase 8.1"""
from random import randint
limitemayor = int(input("Ingrese su limite mayor para generar el numero: "))
limitemenor = int(input("Ingrese su limite menor para generar el numero: "))
num = randint(limitemenor, limitemayor)
if num % 2 == 0:
    print(
        f"El numero aleatorio es: {num} el cual es par, fantástico con este número se generará la tabla de multiplicar")
else:
    if num == limitemenor:
        num += 1
    else:
        num -= 1
    print(f"El numero aleatorio es impar, se dejará como numero para generar la tabla de multiplicar el {num}")
print(f"Tabla de multiplicar del {num}")
print(f'''
      {num}x1 = {num}
      {num}x2 = {num * 2}
      {num}x3 = {num * 3}
      {num}x4 = {num * 4}
      {num}x5 = {num * 5}
      {num}x6 = {num * 6}
      {num}x7 = {num * 7}
      {num}x8 = {num * 8}
      {num}x9 = {num * 9}
      {num}x10 = {num * 10}
      {num}x11 = {num * 11}
      {num}x12 = {num * 12}
      ''')
