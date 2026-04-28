"""Ejercicios de mi brochatgpt"""
# numeros = []
# for i in range(1,6):
#     num = int(input("Ingrese un numero: "))
#     numeros.append(num)
# print(f"Los numeros ingresados son los siguientes: {numeros}")
# maximo = max(numeros)
# print(f"El numero mas grande ingresado fue el: {maximo}")
# print(f"El promedio de los numeros que ingreso es: {sum(numeros)/len(numeros)}")
########################################################
# numeros = []
# num = 1
# while num != 0:
#     num = int(input("Ingrese numeros hasta que desea salir (SALIR = 0): "))
#     if num != 0:
#         numeros.append(num)
# print(f"Numeros ingresados: {len(numeros)}")
# if len(numeros) > 0:
#     prom = sum(numeros) / len(numeros)
#     print(f"El promedio de sus numeros es: {prom}")
#     print("Numeros mayores al promedio: ")
#     for num in numeros:
#         if num > prom:
#             print(num)
# else:
#     print("No se ingresaron numeros")
############################################################
lista = []
while True:
    print("1) Agregar Numero \n2) Mostrar Lista \n3) Mostrar promedio \n4) Mostrar numeros mayores al promedio \n5) Salir")
    op = int(input("Seleccione 1-5: "))
    match op:
        case 1:
            num = int(input("Ingrese el numero a agregar a su lista: "))
            if num > 0:
                lista.append(num)
            else:
                print("El numero 0 no se considerara para su lista")
        case 2:
            if len(lista) > 0:
                print(f"Los numeros de su lista son: {lista}")
            else:
                print("No a ingresado ningun numero aun")
        case 3:
            if len(lista) > 0:
                print(f"El promedio es: {sum(lista) / len(lista)}")
            else:
                print("Aun no a ingresado ningun numero ;c")
        case 4:
            if len(lista) > 0:
                prom = sum(lista) / len(lista)
                print("Los numeros mayores al promedio son: ")
                for num in lista:
                    if num > prom:
                        print(num)
            else:
                print("Aun no ingresas numeros ;c")
        case 5:
            print("Gracias por probar mi programa =)")
            break