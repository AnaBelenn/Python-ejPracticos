'''
Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. El programa debe estar 
preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.
'''
confirmacion=input("Desea comenzar la compra? S/N\n").upper()
total=0
while confirmacion=="S":
    cantidad=int(input("Ingrese cantidad del producto:\n"))
    precio=float(input("Ingrese precio del producto:\n$"))
    total= total + (cantidad*precio)
    confirmacion=input("Desea continuar? S/N\n").upper()
print(f"Total de la compra: ${total}")