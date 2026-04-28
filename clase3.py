"""Clase 3"""
nombre = input("Ingrese su nombre: ")
peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print(f"{nombre} tu IMC es de {imc:.2f}")
if imc < 18.5:
    print("Estas bajo peso")
elif imc == 18.5 and imc < 24.9:
    print("Esta saludable")
elif imc == 25 and imc < 29.9:
    print("Esta sobrepeso")
else:
    print("Esta obeso")
