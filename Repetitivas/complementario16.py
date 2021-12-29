'''
Escribir un programa el cual lea dos valores enteros. Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. Si el 
segundo es menor que el primero, que imprima el mensaje ``Abajo''. Si los números son iguales, que imprima el mensaje ``igual''. Si alguno 
de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''.
'''
conf=input("Desea comenzar? S/N\n").upper()
while conf == "S":
    valor1=int(input("Ingrese el primer valor: \n"))
    valor2=int(input("Ingrese el segundo valor: \n"))
    if valor1==0 or valor2==0:
        print("Error")
        continue
    elif valor1<valor2:
        print("Arriba")
    elif valor1>valor2:
        print("Abajo")
    else:
        print("Igual")
    conf=input("Desea continuar? S/N\n").upper()
print("Fin del programa.")