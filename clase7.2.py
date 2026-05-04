"""Clase 7, Ejercicio de juego con numeros"""
from random import randint
print("En este juego debera adivinar un numero entre el 1 y el 50")
num = randint(1,50)
oportunidades = 4
while oportunidades>0:
    print(f"Tienes {oportunidades} oportunidades")
    numeropersona = int(input("Ingrese su numero: "))
    diferencia = abs(num - numeropersona)
    if numeropersona == num:
        print("GANASTE WONS🔥😍🥹")
    else:
        if diferencia >= 1 and diferencia <= 10:
            print("Caliente")
        elif diferencia >= 11 and diferencia <= 20:
            print("Tibio")
        else:
            print("Frio")
    oportunidades -= 1
    if oportunidades == 0:
        print(f"Perdiste, el numero era {num} 😔")
