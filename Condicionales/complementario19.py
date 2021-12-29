'''
Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el siguiente criterio:
i) A librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.
ii) A particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.
El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. Dado el importe bruto de una compra de libros, el tipo de 
cliente de que se trata y la cantidad total pedida por el mismo, determinar el importe bruto bonificado.
'''
cantidad=int(input("Ingrese cantidad de libros:\n"))
cliente=input("Seleccione tipo de cliente: \n'L' librerías\n'P' particulares\n").upper()
monto=float(input("Ingrese monto de la compra:\n"))
if cliente == "L":
    if cantidad<=24:
        descuento=monto-(monto*0.2)
    else:
        descuento=monto-(monto*0.25)
elif cliente == "P":
    if cantidad<6:
        descuento=monto
        print("No posee descuento.")
    elif cantidad>=6 and cantidad<=18:
        descuento=monto-(monto*0.05)
    else:
        descuento=monto-(monto*0.1)
print(f"Cantidad de libros comprados: {cantidad}\nImporte bruto a pagar: ${descuento}")
