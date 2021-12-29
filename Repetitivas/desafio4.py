'''
Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. Por ejemplo el gráfico a la 
izquierda es el resultado de un tamaño: 8x6
SIN COMPLETAR. 
'''

verde = ('\x1b[6;30;42m' + '  ' + '\x1b[0m') 
blanco= ('\x1b[0;30;47m' + '  ' + '\x1b[0m')
filas =int(input("Ingrese numero de filas:\n"))
col = int(input("Ingrese numero de columnas:\n"))
for i in range(0, filas):
    for j in range(0, col):
        if i%2 !=0:
            print(verde + blanco)
        else:
            print(blanco + verde)

print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
