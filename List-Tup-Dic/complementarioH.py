'''
Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''
lista=[5, 4, 3, 8, 9, 12, 7, 6, 2, 1, 5]
suma=0
nueva_lista=list()
for n in range(len(lista)):
    if n%2==0:
        nueva_lista.append(lista[n])
        suma+= lista[n]
print(f"Elementos que se sumaron: {nueva_lista}\nSumatoria: {suma}")