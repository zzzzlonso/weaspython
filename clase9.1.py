"""Clase 9.1"""
from random import randint
puntos = 0
puntospc = 0
op = int(input("Eliga (1) Piedra 2) Papel 3) Tijera) "))
eleccionpc = randint(1,3)
if op == eleccionpc:
    print("Empate")
elif (op == 1 and eleccionpc == 3) or (op == 2 and eleccionpc == 1) or (op == 3 and eleccionpc == 2):
    print("Ganaste 5 puntos")
    puntos += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
elif (eleccionpc == 1 and op == 3) or (eleccionpc == 2 and op == 1) or (eleccionpc == 3 and op == 2):
    print("PC gano 5 puntos")
    puntospc += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
else:
    print("Escogiste mal")
op = int(input("Eliga (1) Piedra 2) Papel 3) Tijera) "))
eleccionpc = randint(1,3)
if op == eleccionpc:
    print("Empate")
elif (op == 1 and eleccionpc == 3) or (op == 2 and eleccionpc == 1) or (op == 3 and eleccionpc == 2):
    print("Ganaste 5 puntos")
    puntos += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
elif (eleccionpc == 1 and op == 3) or (eleccionpc == 2 and op == 1) or (eleccionpc == 3 and op == 2):
    print("PC gano 5 puntos")
    puntospc += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
else:
    print("Escogiste mal")
op = int(input("Eliga (1) Piedra 2) Papel 3) Tijera) "))
eleccionpc = randint(1,3)
if op == eleccionpc:
    print("Empate")
elif (op == 1 and eleccionpc == 3) or (op == 2 and eleccionpc == 1) or (op == 3 and eleccionpc == 2):
    print("Ganaste 5 puntos")
    puntos += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
elif (eleccionpc == 1 and op == 3) or (eleccionpc == 2 and op == 1) or (eleccionpc == 3 and op == 2):
    print("PC gano 5 puntos")
    puntospc += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
else:
    print("Escogiste mal")
op = int(input("Eliga (1) Piedra 2) Papel 3) Tijera) "))
eleccionpc = randint(1,3)
if op == eleccionpc:
    print("Empate")
elif (op == 1 and eleccionpc == 3) or (op == 2 and eleccionpc == 1) or (op == 3 and eleccionpc == 2):
    print("Ganaste 5 puntos")
    puntos += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
elif (eleccionpc == 1 and op == 3) or (eleccionpc == 2 and op == 1) or (eleccionpc == 3 and op == 2):
    print("PC gano 5 puntos")
    puntospc += 5
    print(f"Puntos actuales: PC {puntospc}, TU {puntos}")
else:
    print("Escogiste mal")
if puntospc > puntos:
    print("Gano: PC")
elif puntos == puntospc:
    print("Empataron")
else:
    print("Ganaste")