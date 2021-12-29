'''
Determinar el número mayor de 10 números ingresados.
'''
num=0
may=0
for n in range(10):
    num=(int(input("Ingrese un numero:\n")))
    if num>may:
        may=num
print(f"El mayor de los numeros ingresados es: {may}")
