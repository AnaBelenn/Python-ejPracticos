'''
Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
'''
n1=int(input("Ingrese el primer numero:\n"))
n2=int(input("Ingrese el segundo numero:\n"))
if n1==n2:
    print(f"Producto de {n1} x {n2} = {n1*n2}")
elif n1>n2:
    print(f"Resta entre {n1} - {n2} = {n1-n2}")
else:
    print(f"Suma entre {n1} + {n2} = {n1+n2}")