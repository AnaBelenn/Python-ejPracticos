'''
Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
'''
print("Producto entre A x B.")
a=int(input("Ingrese el numero entero A:\n"))
b=int(input("Ingrese el numero entero B:\n"))
resultado=0
for n in range(b):
    resultado=resultado+a
print(f"Resultado: {resultado}")