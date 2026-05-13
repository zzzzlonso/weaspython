"""CLASE 8"""
subtotal = 0
desc = 0
precioM = 0
flag = 0
print("""
Concepto 	          Rango	             Valor 
Matrícula básica	1ro a 8vo	        $45.000
Matrícula media	        1ro a 4to	        $67.000
Centro de padres	Todos los cursos	$10.000
Mensualidad	        Todos los cursos	$30.000
      """)
print("1) Matricula Básica")
print("2) Matricula Media")
matricula = int(input("Que matricula va a Pagar (1/2): "))
if matricula == 1:
    precioM = 45000
    flag += 1
elif matricula == 2:
    precioM = 67000
    flag += 1
else:
    print("No registra matricula")
subtotal += precioM
padres = input("Pagara centro de padres? (S/N): ").upper()
if padres == "S":
    subtotal += 10000
    print("Usted paga $10000 por centro de padres")
    flag += 1
else:
    print("No paga centro de padres")
mensualidad = input("Pagara mensualidades? (S/N): ").upper()
if mensualidad == "S":
    cantidad = int(input("Cuantas mensualidades pagara? (1/12): "))
    if 3 <= cantidad <= 5:
        desc = 0.06
        print("Posee descuento del 6%")
    elif 6 <= cantidad <=12:
        desc = 0.1
        print("Posee descuento del 10%")
        if cantidad == 12:
            flag += 1
    else:
        print("No posee descuento")
preciomensualidad = (cantidad * 30000)-(cantidad * 30000 * desc)
print(f"Su total a pagar en mensualidad es: {int(preciomensualidad)}")
subtotal += preciomensualidad
print(f"Su total a pagar es: {int(subtotal)}")
if flag == 3:
    print("Por pagar todo obtiene un descuento extra del 20%")
    subtotal -= subtotal * 0.2
    print(f"Su nuevo total es: {int(subtotal)}")
