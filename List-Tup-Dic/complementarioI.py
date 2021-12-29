'''
Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.
'''
lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista2=list()
for n in range(15):
    if lista1[n]%2==0:
        lista2.append((lista1[n])*2)
print(lista1)
print(lista2)