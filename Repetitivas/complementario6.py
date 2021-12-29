'''
Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.
'''
inicio=int(input("Ingrese el inicio del rango:\n"))
fin=int(input("Ingrese el fin del rango:\n"))
print("Numeros múltiplos de 2 dentro del rango establecido:\n")
contador=0
suma=0
if inicio<fin:
    for n in range(inicio, fin+1):
        if n%2==0:
            print(n)
            contador+=1
            suma+=n
elif inicio>fin:
    for n in range(inicio, fin, -1):
        if n%2==0:
            print(n)
            contador+=1
            suma+=n
else:
    print("Los numeros ingresados son iguales.")
print(f"Cantidad de numeros multiplos de 2: {contador}\nSuma de los multiplos de 2: {suma}")