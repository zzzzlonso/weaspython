"""parte2"""
acum = 0
while True:
    print("1) Registrar Actividades")
    print("2) Mostrar analisis del tiempo")
    print("3) Salir")
    op = int(input("Seleccione 1-3: "))
    match op:
        case 1:
            print("Registro de actividades: ")
            cant_act = int(input("Ingrese cantidad de actividades : "))
            if cant_act >= 3:
                for i in range (1, cant_act + 1):
                    actividad = input(f"Ingrese el nombre de su actividad {i}")
                    tiempo = int(input("Cuantos minutos se demora en esta actividad: "))
                    acum = acum + tiempo
            else:
                print("Minimo debe declarar 3 actividades")
        case 2:
            print("Analisis de tiempo: ")
            print ("Su total en minutos es: ", acum)
            if acum > 180:
                print("Tiene un tiempo excesivo en sus actividades")
            else:
                print("Tiene un tiempo normal")
        case 3:
            print("Fin proceso")
            break
        case _:
            print("Elige bien compita")
