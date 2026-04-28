"""Ejercicio"""
total= 0
price = 0
print("1) Lipigas      15 Kilos    $15.500")
print("2) Gasco        11 Kilos    $10.000")
print("3) Gasco        15 Kilos    $13.000")
print("4) Abastible    45 Kilos    $45.000")
op = int(input("Que opcion necesita: "))
cantidad = int(input("Cuantos desea comprar: "))
if op == 1:
    price = 15000
elif op == 2:
    price = 10000
elif op == 3:
    price = 13000
elif op == 4:
    price = 45000
else: 
    print("Escogio incorrectamente")
if cantidad > 0:
    subtotal = price * cantidad
    if cantidad > 2 and op != 2:
        if op == 1:
            total = subtotal * 0.9
        elif op == 3:
            total = subtotal * 0.95
        elif op == 4:
            total = subtotal * 0.97
print (f"Subtotal: {subtotal}")
if total == subtotal:
    print("No cuenta con descuentos")
else:
    print(f"Aplica a descuento: {total}")
print(f"Iva: {total*0.19}")
print(f"Total: {total*1.19}")
