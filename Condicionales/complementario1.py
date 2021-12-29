'''
Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
'''
numeros=list()
for i in range(3):
    numeros.append(int(input("Ingrese un numero:\n")))
print(sorted(numeros, reverse=True))