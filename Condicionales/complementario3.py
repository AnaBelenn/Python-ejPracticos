'''
Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.
'''
a=int(input("Ingrese el primer numero:\n"))
b=int(input("Ingrese el segundo numero:\n"))
c=int(input("Ingrese el tercer numero:\n"))
if a<b and a<c:
    print(f"El numero {a} es menor que {b} y {c}")
else:
    print(f"{a} no es el menor de los tres numeros ingresados.")