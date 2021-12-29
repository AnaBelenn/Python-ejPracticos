'''
En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el número escogido es menor que 50 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 50 el descuento es del 20%. 
Obtener cuánto dinero se le descuenta.
'''
import random
conf=input("Para iniciar presione S - Para salir presione N\n").upper()
while conf == "S":
    nro_random=random.randint(0, 100)
    compra=float(input("Ingrese monto de la compra: $"))
    if nro_random<50:
        total=compra-compra*0.15
        print(f"Numero obtenido: {nro_random}\nObtuvo un descuento del 15%\nDescuento = ${round((compra*0.15), 2)}")
    else:
        print(f"Numero obtenido: {nro_random}\nObtuvo un descuento del 20%\nDescuento = ${round((compra*0.2), 2)}")
        total=compra-compra*0.20
    print(f"Monto total a pagar = ${total}")
    conf=input("Para continuar presione S - Para salir presione N\n").upper()
print("Fin del programa.")