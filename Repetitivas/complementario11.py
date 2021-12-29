'''
Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.
'''
numero=int(input("Ingrese un numero: \n"))
print(f"Divisores de {numero}:")
for n in range(1, numero+1):
    if numero%n==0:
        print(n)
print("Fin del programa.")