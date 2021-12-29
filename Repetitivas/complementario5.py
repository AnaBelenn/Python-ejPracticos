'''
Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. El ciclo debe finalizar cuando el usuario
ingresa 0.
'''
numero=int(input("Ingrese un numero para determinar si es par o impar, o presione 0 para salir: \n"))
while numero != 0:
    if numero%2==0:
        print(f"{numero} es par.\n")
    else:
        print(f"{numero} es impar.\n")
    numero=int(input("Ingrese un numero para determinar si es par o impar, o presione 0 para salir: \n"))
print("Fin del programa.")