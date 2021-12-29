'''
En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para 
reciclar, de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. 
Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 
Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento.
'''
conf=input("Desea ingresar una compra? S/N\n")
conf= conf.upper()
while conf == "S":
    compra=int(input("Ingrese el monto de la compra:\n"))
    descuento=input("Ingrese el color del descuento:\n")
    descuento = descuento.lower()
    if descuento == "rojo":
        print("Posee un descuento del 40%")
        compra=compra - (compra*0.4)
    elif descuento == "amarillo":
        print("Posee un descuento del 25%")
        compra=compra - (compra*0.25)
    else:
        print("No posee descuento.")
    print(f"Monto total a pagar: ${compra}\n¡ Gracias por su compra !")
    conf = input("Desea ingresar otra compra? S/N \n")
    conf = conf.upper()
print("Fin de la jornada.")
