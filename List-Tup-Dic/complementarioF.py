'''
Cargar k elementos en una cola, y luego copiarlos en una nueva lista.
'''
cola=list()
lista=list()
k=int(input("Cantidad de elementos: \n"))
for n in range(k):
    cola.append(input("Ingrese elemento:\n"))
lista=cola[:]
print(lista)