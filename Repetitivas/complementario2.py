'''
Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
'''
resultado=0
cantidad=int(input("Hasta que numero desea contar?\n"))
for n in range(cantidad):
    resultado = resultado + (n**2)
print(f"Se contaron {cantidad} numeros y la suma de sus cuadrados es igual a {resultado}")