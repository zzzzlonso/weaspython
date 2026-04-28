"""clase 3.2"""
total = 0
compra = int(input("Valor Primera compra:"))
if compra > 100:
    total += compra
compra2 = int(input("Valor segunda compra: "))
if compra2 > 100:
    total += compra2
compra3 = int(input("Valor 3ra compra: "))
if compra3 > 100:
    total += compra3
print(f"el total es de {total} en compras superiores a 100 pesos")
print(f"El IVA de este compra es de ${total*0.19}")
