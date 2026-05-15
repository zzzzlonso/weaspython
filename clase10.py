"""Clase 10"""
totalingresos = 0
while True:
    try:
        cant = int(input("Cuantos pasajes desea vender: "))
        break
    except ValueError as error:
        print("Debe ingresar algun numero")
        cant = 0
for i in range(cant):
    while True:
        try:
            totalingresos += int(input(f"Ingrese el precio del pasaje {i+1}: "))
        except ValueError as error:
            print("Debia ingresar un valor valido como numero")
            break
print(f"El total es: ${totalingresos}")
# print(f"El total es de ${totalingresos}")
# videojuegos = {}
# mayores40 = []
# mayor_precio = 0
# juegomayor = ""
# for i in range(4):
#     nombre = input("Ingrese el nombre de su videojuego: ")
#     precio = int(input("Ingrese el precio del videojuego: "))
#     genero = input("Ingrese el genero del juego: ")
#     videojuegos[nombre] = {"PRECIO": precio, "GENERO": genero}
# print("Lista de juegos")
# for nombre, datos in videojuegos.items():
#     print(f"{nombre}")
#     if datos["PRECIO"] > 40000:
#         mayores40.append(nombre)
#     if datos["PRECIO"] > mayor_precio:
#         mayor_precio = datos["PRECIO"]
#         juegomayor = nombre 
# print(f"El juego mas caro es {juegomayor} con un precio de {mayor_precio}")
# print("Juegos con precios mayores a $40000")
# for name in mayores40:
#     print(f"{name}")
