'''
Desarrolle un programa que permita determinar si un número X ingresado es par o impar.
'''
num=int(input("Ingrese un numero:\n"))
if num%2==0:
    print(f"{num} es un numero PAR.")
else:
    print(f"{num} es un numero IMPAR.")