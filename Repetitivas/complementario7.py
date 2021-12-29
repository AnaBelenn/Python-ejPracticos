'''
Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. El programa no permitirá 
introducir valores negativos para A y B y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
'''
a=int(input("Ingrese el inicio del rango:\n"))
b=int(input("Ingrese el fin del rango:\n"))
contador=0
suma=0
if a<0 or b<0:
    print("No se permiten valores negativos.")
    band=False
elif a>b:
    c=a
    a=b
    b=c
    band=True
elif a==b:
    print("Los numeros ingresados son iguales.")
    band=False

if band==True:
    for n in range(a, b):
        if n%5==0:
            print(n)
            contador+=1
            suma+=n
    print(f"Cantidad de numeros multiplos de 5: {contador}\nSuma de los multiplos de 5: {suma}")