"""Ejercicio 6"""
# aprob = None
# alumnos = ["Ana", "Pedro", "Luis", "María", "Carlos"]
# notas = [72, 45, 88, 61, 39]
#######################################
# for n in range(len(alumnos)):
#     if notas[n] >= 60:
#         aprob = "Aprobado"
#     else:
#         aprob = "Reprobado"
#     print(f"{alumnos[n]} → {notas[n]} → {aprob}")
###############################3
# alumnos = {}
# alumnos["Ana"] = {"nota": 72 , "carrera": "Informatica", "aprobado": "Aprobado"}
# alumnos["Juan"] = {"nota": 50 , "carrera": "Contabilidad", "aprobado": "Desaprobado"}
# alumnos["Dominique"] = {"nota": 90 , "carrera": "Psicología", "aprobado": "Aprobado"}
# for nombre, datos in alumnos.items():
#     print(f"{nombre} = {datos["nota"]} |Carrera: {datos["carrera"]} = {datos["aprobado"]}")
##############################################
# productos = {}
# for i in range(3):
#     nombre = input("Ingrese el nombre de su producto: ")
#     valor = int(input("Ingrese el valor del producto: "))
#     stock = int(input("Ingrese el stock del producto: "))
#     productos[nombre] = {"Precio": valor, "Stock": stock}
# for nombre, datos in productos.items():
#     if datos["Stock"] < 5:
#         stock = "⚠️ Stock bajo"
#     else:
#         stock = " "
#     print(f"{nombre} = Precio: ${datos["Precio"]} | Stock: {datos["Stock"]} {stock}")
############################################################
# numeros = [15, 42, 8, 97, 23, 56, 4, 78, 31, 63]
# print(f"El numero mayor es: {max(numeros)} y el menor es: {min(numeros)}")
# numeros.sort(reverse=True)
# print(numeros)
# print("Numeros mayores a 50: ")
# for num in numeros:
#     if num > 50:
#         print(num)
#####################################################################
# paises = {}
# for i in range(3):
#     pais = input("Ingrese el pais: ")
#     capital = input("Ingrese la capital")
#     poblacion = int(input("Ingrese la poblacion del pais en MILLONES: "))
#     paises[pais] = {"Capital":capital, "Poblacion":poblacion}
# for nombre, datos in paises.items():
#     if datos["Poblacion"] > 10:
#         print(f"{nombre} → Capital: {datos["Capital"]} |Poblacion: {datos["Poblacion"]} millones")
#############################################3
alumnos = {}

# for i in range(4):
#     alumno = input("Ingrese nombre del alumno")
#     nota1 = int(input("Ingrese la primera nota: "))
#     nota2 = int(input("Ingrese la segunda nota: "))
#     nota3 = int(input("Ingrese la tercera nota: "))
#     notas = []
#     notas.append(nota1)
#     notas.append(nota2)
#     notas.append(nota3)
#     alumnos[alumno] = {"notas": notas}
# for alumno, datos in alumnos.items():
#     prom = sum(datos["notas"]) / len(datos["notas"])
#     if prom >= 60:
#         aprob = "Aprobado"
#     else:
#         aprob = "Desaprobado"
#     print(f"{alumno}: → Promedio: {prom} | {aprob}")
    #####################################################
# palabras = ["gato", "perro", "gato", "pez", "perro", "gato", "loro"]
# conteo = {}
# for animales in palabras:
#     if animales in conteo:
#         conteo[animales] += 1
#     else:
#         conteo[animales] = 1
# for animal, cantidad in conteo.items():
#     print(f"{animal} → {cantidad}")
##################################################
# amigos = {}
# for i in range (5):
#     nombre = input("Ingrese el nombre del amigo: ")
#     dinero = int(input("Ingrese el aporte monetario de ese amigo: "))
#     amigos[nombre] = {"Dinero": dinero}
# total = 0
# minimo = 0
# maximo = 0
# mayor = ""
# menor = ""
# for nombre, datos in amigos.items():
#     if datos["Dinero"] > maximo:
#         maximo = datos["Dinero"]
#         mayor = nombre
#     if total == 0:
#         minimo = datos["Dinero"]
#         menor = nombre
#     elif total > 0:
#         if datos["Dinero"] < minimo:
#             minimo = datos["Dinero"]
#             menor = nombre
#     total += datos["Dinero"]
# print(f"Total acumulado: {total}")
# print(f"Mayor aporte de: {mayor}")
# print(f"Menor aporte de: {menor}")
# if total > 50000:
#     print("✅ Alcanza para el regalo")
# else:
#     print("❌ Falta plata")
############################################
# candidatos = ["ANA", "GABRIEL", "FABIAN"]
# votos = {}
# for candidato in candidatos:
#     votos[candidato] = 0
# while True:
#     voto = input("Ingrese el candidato a votar('fin' para salir): ").upper()
#     if voto in votos:
#         votos[voto] += 1
#     elif voto == "FIN":
#         print("---Resultados---")
#         break
#     else:
#         print("Candidato invalido") 
# for nombre, voto in votos.items():
#     print(f"{nombre} → {voto} votos")
# ganador = max(votos, key=votos.get)
# print(f"El ganador fue: {ganador}")
##################################################33
# playlist = ["USSEEWA", "NEW GENESIS", "ODO", "GIRA GIRA", "TOT MUSICA"]
# num = 1
# for i in range(len(playlist)):
#     print(f"{i+1}. {playlist[i]}")
# eliminar = input("Que cancion desea eliminar: ").upper()
# if eliminar in playlist:
#     playlist.remove(eliminar)
# else:
#     print("Esa cancion no esta en la playlist")
# print("Playlist actualizada: ")
# for i in range(len(playlist)):
#     print(f"{i+1}. {playlist[i]}")
####################################################

