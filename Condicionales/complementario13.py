'''
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es del 20%. 
Obtener cuánto dinero se le descuenta.
'''
import random
nro_random=random.randint(0, 100)
compra=float(input("Ingrese total de la compra: \n$"))
if nro_random<74:
    descuento=compra*0.15
    print(f"El numero escogido es {nro_random}. Tiene un 15% de descuento !\nEl total de su compra es: ${compra}\nDescuento: ${descuento}\nMonto final a pagar: ${compra-descuento}")
else:
    descuento=compra*0.2
    print(f"El numero escogido es {nro_random}. Tiene un 20% de descuento !\nEl total de su compra es: ${compra}\nDescuento: ${descuento}\nMonto final a pagar: ${compra-descuento}")
