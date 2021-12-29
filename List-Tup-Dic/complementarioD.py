'''
Realice una función que dada una lista de enteros L, y un número entero n. Elimine de la lista original los elementos que sean iguales a 
ese número dado.
'''
l=[1, 2, 5, 6, 9, 5, 4, 1, 5, 2, 5]
n=int(input("Ingrese el numero que desea eliminar:\n"))
for elto in l:
    if elto==n:
        l.remove(elto)
print(l)