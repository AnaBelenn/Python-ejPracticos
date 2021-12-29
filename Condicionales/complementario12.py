'''
Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. El descuento lo hace en base a la 
clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).
'''
articulo=input("Ingrese el nombre del articulo: \n")
precio_original=float(input("Ingrese precio: \n$"))
clave=int(input("ingrese la clave: \n"))
if clave == 1:
    precio_descuento=precio_original - (precio_original*0.1)
elif clave == 2:
    precio_descuento= precio_original - (precio_original*0.2)
print(f"Producto: {articulo}\nPrecio original: ${precio_original}\nPrecio con descuento: ${precio_descuento}")
