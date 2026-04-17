"""CLASE"""
variable_entera = 51
variable_deciamal = 1.232
variable_texto = "chaomundo"
variable_booleana = True


#Crear aplicacion que permita ingresar 3 notas y promediarlas
n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 1: "))
promedio = (n1 + n2 + n3)/3
print("Su promedio es: ", promedio)
if promedio >= 4:
    print("Aprobado")
else:
    print("Reprobado")
