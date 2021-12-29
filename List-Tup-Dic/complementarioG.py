'''
Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.
'''
lista1=list()
lista2=list()
cantidad=int(input("Cantidad de elementos:\n"))
for elto in range(cantidad):
    lista1.append(input("Ingrese elemento de la primera lista:\n"))
    lista2.append(input("Ingrese elemento de la segunda lista:\n"))
lista1.extend(lista2)
print(sorted(lista1))