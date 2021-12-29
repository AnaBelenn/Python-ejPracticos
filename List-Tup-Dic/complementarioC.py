'''
Escriba un algoritmo que permita cargar una lista. Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.
'''
cantidad=int(input("Cantidad de elementos que desea cargar: \n"))
lista=list()
for n in range(cantidad):
    lista.append(int(input("Ingrese un numero: \n")))

for n in range(cantidad):
    if lista[n]<0:
        lista[n]=0
print(lista)