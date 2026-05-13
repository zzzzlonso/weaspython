"""Ejercicio Fast Racing"""
precio = 0
nombre = ""
desc = 0
print("""
Servicio	         Valor	           Descuento por Club
1) Cambio de aceite	$45.000	                 10%
2) Alineación	    $25.000	                 5%
3) Cambio de frenos	$120.000	         12%
4) Scanner automotriz	$18.000	             3%
        """)
op = int(input("Seleccione del 1 al 4: "))
club = input("Pertenece al Fast Racing Club (S/N): ").upper()
edad = input("Es adulto mayor (S/N): ").upper()
efect = input("Pagara en efectivo (S/N): ").upper()
if op == 1:
    precio = 45000
    nombre = "Cambio de aceite"
    desc = 10
elif op == 2:
    precio = 25000
    nombre = "Alineacion"
    desc = 5
elif op == 3:
    precio = 120000
    nombre = "Cambio de frenos"
    desc = 12
elif op == 4:
    precio = 18000
    nombre = "Scanner automotriz"
    desc = 3
print(f"{nombre}: ${precio}")
if club == "S":
    descuento = desc / 100
    print(f"Descuento club {desc}%: ${precio * descuento}")
    precio -= precio * descuento
else:
    print("No posee descuento club")
if edad == "S":
    print("Descuento adulto mayor: $7000")
    precio -= 7000
else:
    print("No posee descuento adulto mayor")
if efect == "S":
    print("Descuento pago efectivo: $3000")
    precio -= 3000
else:
    print("No posee descuento pago efectivo")
print(f"Total a pagar: ${precio}")
