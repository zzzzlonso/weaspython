"""Clase 9"""
precio = 0
desc = 0
comuna = 0
nombre = ""
descuento = 0
print("""
              Cilindro 	     Valor	  Comuna 	Descuento
1) Abastible  15 Kilos	    $28.000	  Maipú	        5%
2) Abastible  11 Kilos	    $24.000	  Maipú	        8%
3) Gasco      15 Kilos	    $32.000	  La Florida	4%
4) Lipigas de 11 Kilos	    $20.200	  La Granja	    6%
      """)
op = int(input("Seleccion del 1/4: "))
comunavive = input("Indique la comuna donde vive: ")
edad = input("Es tercera edad (S/N): ")
cupon = input("Posee cupon de descuento (S/N): ")

if op == 1: 
    precio = 28000
    comuna = "MAIPU"
    desc = 5
    nombre = "Abastible 15 Kilos"
elif op == 2:
    precio = 24000
    comuna = "MAIPU"
    desc = 8
    nombre = "Abastible 11 Kilos"
elif op == 3:
    precio = 32000
    comuna = "LA FLORIDA"
    desc = 4
    nombre = "Gasco 15 Kilos"
elif op == 4:
    precio = 20200
    comuna = "LA GRANJA"
    desc = 6
    nombre = "Lipigas 11 Kilos"
print(f"{nombre}: {precio}")
descuento = desc / 100
if comunavive == comuna:
    print(f"Descuento del {desc}% por vivir en {comunavive} del {precio-(precio * descuento)}")
    precio -= precio * descuento
else:
    print("No posee descuento por comuna")
if edad.upper() == "S":
    print ("Descuento tercera edad: 5000")
    precio -= 5000
else:
    print("No posee descuento de tercera edad")
if cupon.upper() == "S":
    print("Descuento de cupon: 15000")
    precio -= 15000
else:
    print("No posee descuento de cupon")
print(f"Total a pagar: {precio}")
    