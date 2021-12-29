'''
Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica un descuento del 20% 
sobre el total de la compra y si son menos de tres camisas un descuento del 10%.
'''
camisas=int(input("Cuantas camisas compró?\n"))
compra=float(input("Ingrese el total de la compra: \n$"))
if camisas>=3:
    total=compra-(compra*0.2)
else:
    total=compra-compra*0.1
print(f"Cantidad de camisas: {camisas}\nMonto inicial: ${compra}\nTotal con descuento: ${total}")